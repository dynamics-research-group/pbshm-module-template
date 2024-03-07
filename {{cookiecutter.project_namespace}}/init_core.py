import importlib
import importlib.util
import json
import os
import site
import sys

from flask import Flask

def create_app(test_config=None):
    # Create Flask App
    app = Flask(__name__, instance_relative_config=True)

    # Load Configuration
    app.config.from_mapping(
        PAGE_SUFFIX=" - PBSHM Debug & Development",
        LOGIN_MESSAGE="PBSHM Debug & Development Mode: Enter your authentication credentials below.",
        FOOTER_MESSAGE="PBSHM Debug & Development - PBSHM {{ cookiecutter.module_name }}",
        NAVIGATION={
            "modules":{
                "{{ cookiecutter.module_name }}" : "{{ cookiecutter.__project_slug }}.module_homepage",
                "Help": "layout.home"
            }
        }
    )
    app.config.from_file("config.json", load=json.load, silent=True) if test_config is None else app.config.from_mapping(test_config)

    # Ensure Instance Folder
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Calculate site packages folder
    pbshm_directory, package_paths = None, site.getsitepackages()
    selected_package_path = os.path.join(package_paths[1 if len(package_paths) > 1 and sys.platform == "win32" else 0], "pbshm")
    if os.path.isdir(selected_package_path): pbshm_directory = selected_package_path
    else:
        for path in package_paths:
            potential_path = os.path.join(path, "pbshm")
            if potential_path == selected_package_path:
                continue
            elif os.path.isdir(potential_path):
                pbshm_directory = potential_path
                break
    if pbshm_directory is None:
        raise Exception(f"Unable to find site packages with the PBSHM namespace, paths searched: {package_paths}")

    # Include PBSHM Core Packages
    importlib.invalidate_caches()
    pbshm_modules = {
        "pbshm.db": {
            "path": ["db.py"],
            "blueprint": False,
            "url_prefix": None
        },
        "pbshm.mechanic": {
            "path": ["mechanic", "__init__.py"],
            "blueprint": True,
            "url_prefix": None
        },
        "pbshm.initialisation": {
            "path": ["initialisation", "__init__.py"],
            "blueprint": True,
            "url_prefix": None
        },
        "pbshm.authentication": {
            "path": ["authentication", "__init__.py"],
            "blueprint": True,
            "url_prefix": "/authentication"
        },
        "pbshm.layout": {
            "path": ["layout", "__init__.py"],
            "blueprint": True,
            "url_prefix": "/layout"
        },
        "pbshm.timekeeper": {
            "path": ["timekeeper", "__init__.py"],
            "blueprint": True,
            "url_prefix": "/timekeeper"
        }
    }
    
    for module_name in pbshm_modules:
        print(f"Loading PBSHM Module: {module_name}")
        module_spec = importlib.util.spec_from_file_location(module_name, os.path.join(pbshm_directory, *pbshm_modules[module_name]["path"]))
        module = importlib.util.module_from_spec(module_spec)
        sys.modules[module_name] = module
        module_spec.loader.exec_module(module)
        if pbshm_modules[module_name]["blueprint"]:
            app.register_blueprint(module.bp, url_prefix=pbshm_modules[module_name]["url_prefix"])

    # Include Developing Module: {{ cookiecutter.module_name }}
    from {{cookiecutter.project_namespace}} import {{ cookiecutter.__project_slug }} # Note: Must be done after the core modules are loaded in otherwise any references to core modules will fail
    app.register_blueprint({{ cookiecutter.__project_slug }}.bp, url_prefix="/{{ cookiecutter.__project_slug }}")
    
    # Set Root Page
    app.add_url_rule("/", endpoint="{{ cookiecutter.__project_slug }}.module_homepage")

    # Return App
    return app