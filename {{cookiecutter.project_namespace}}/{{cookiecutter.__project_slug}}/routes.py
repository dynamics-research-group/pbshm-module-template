"""
A module containing the logic for showcasing the views of the module.
"""
import json
from flask import Blueprint, render_template
from pbshm.authentication import authenticate_request
from os.path import join, dirname

# Create the module blueprint
bp = Blueprint(
    "{{cookiecutter.__project_slug}}",
    __name__,
    template_folder="templates"
)

@bp.route("/{{ cookiecutter.__project_slug }}/home")
@authenticate_request("{{ cookiecutter.__project_slug }}-home")
def module_homepage():
    with open(join(dirname(__file__), "static/static_file.json"), 'r') as f:
        jsond = json.load(f)
    
    universities = jsond["rosehipsUniversities"]

    return render_template("example.html", module_name="{{ cookiecutter.module_name }}", universities=universities)
