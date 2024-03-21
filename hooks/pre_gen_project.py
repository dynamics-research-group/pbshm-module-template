import sys
import os
import subprocess
import pathlib
import venv
import re

# Validate template variables
first_name = "{{ cookiecutter.first_name }}".strip()
if not first_name:
    raise ValueError("first_name must not be blank.")
if not re.match("^[a-zA-Z]+$", first_name):
    raise ValueError("first_name must contain only alphabetic characters.")

last_name = "{{ cookiecutter.last_name }}".strip()
if not last_name:
    raise ValueError("last_name must not be blank.")
if not re.match("^[a-zA-Z]+$", last_name):
    raise ValueError("last_name must contain only alphabetic characters.")

email = "{{ cookiecutter.email }}".strip()
if not email:
    raise ValueError("email must not be blank.")
if not re.match("^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$", email):
    raise ValueError("email must be a valid email address.")

project_namespace = "{{ cookiecutter.project_namespace }}".strip()
if not project_namespace:
    raise ValueError("project_namespace must not be blank.")
if not re.match("^[a-zA-Z]+$", project_namespace):
    raise ValueError("project_namespace must contain only alphabetic characters.")

if (project_namespace == "pbshm") and ("{{ cookiecutter.project_type }}" == "framework"):
    raise NameError("The namespace 'pbshm' is protected inside the framework installation.")
if (project_namespace == "rosehips"):
    raise NameError("The namespace 'rosehips' is protected inside the framework and core installations.")

module_name = "{{ cookiecutter.module_name }}".strip()
if not module_name:
    raise ValueError("module_name must not be blank.")
if not re.match("^[a-zA-Z\s]+$", module_name):
    raise ValueError("module_name must contain only alphabetic characters.")

version = "{{ cookiecutter.version }}".strip()
if not re.match("^([0-9]+)\\.([0-9]+)\\.([0-9]+)$", version):
    raise ValueError("version must match the format X.Y.Z where X, Y, and Z are non-negative integers.")


# Setting up environment
subprocess_params = {
    "stdout": subprocess.PIPE,
    "stderr": subprocess.PIPE,
    "check": True
}
python_executable = sys.executable  # Use current interpreter. 

# If not currently inside a virtual environment then create one, else use 
# the current virtual environment.
if not "VIRTUAL_ENV" in os.environ:
    parent_dir = pathlib.Path(os.getcwd()).parent.resolve()
    venv_name = "env"  # Could pass this as a param in cookiecutter.json.
    env_path = str(parent_dir / venv_name)

    try:
        # Create the venv, could modify the python version here.
        venv.create(env_path, with_pip=True)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

else:
    env_path = os.environ["VIRTUAL_ENV"]

try:
    # Determine the path to the venv's python executable
    if sys.platform == "win32":
        venv_python = os.path.join(env_path, "Scripts", "python.exe")
    elif sys.platform in ("linux", "linux2"):
        venv_python = os.path.join(env_path, "bin", "python")
    else:
        raise OSError("Unsupported operating system. Currently only Linux and Windows are supported.")

    # Install pbshm core/framework in venv by directly using the venv's python executable
    print("Installing PBSHM", "{{ cookiecutter.project_type }}".title())
    result = subprocess.run([venv_python, "-m", "pip", "install", "pbshm-{{ cookiecutter.project_type }}"], **subprocess_params)
    
    print(f"stdout pip install pbshm-{{ cookiecutter.project_type }}: {result.stdout.decode()}")
    print(f"stderr pip install pbshm-{{ cookiecutter.project_type }}: {result.stderr.decode()}")

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e.output.decode()}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
