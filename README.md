# Installing Modules with PBSHM Flask Core

## Overview
When creating and installing modules, they need to be integrated within the PBSHM Flask Core. This integration ensures that all functionalities available within the core are also accessible from within the module. Using cookiecutter provides a streamlined experience for integrating with the pbshm-flask-core's capabilities.

## Creating a New Module
To create a new module integrated with the PBSHM Flask Core, along with setting up a new environment, you first need to install Cookiecutter. Cookiecutter is a command-line utility that creates projects from templates, allowing for easy module scaffolding.

### Installation Instructions

1. **Install Cookiecutter**: Follow the installation instructions for Cookiecutter to get started. You can find the documentation and installation guidelines at the [Cookiecutter official website](https://cookiecutter.readthedocs.io/en/latest/installation.html).

2. **Generate Module Structure**: Once Cookiecutter is installed, you can generate your new module structure by running the following command in your terminal:

```
cookiecutter https://github.com/TristanGowdridge/module_structure
```

This command will prompt you to enter various details about your new module, ensuring a customised and ready-to-use module structure tailored to your needs.

# Templated Modules Functionality

1. The module created via cookiecutter is simply a scaffold outlining best folder structuring for the easiest module creation.

2. Some base functionality and routing is set which can be expanded upon.

3. A virtual environment is created under the name `env` and the pbhsm-flask-core is installed inside this environment. When running your code, ensure you have activated this environment.

4. When activating the environment, some environment variables have been preset: `FLASK_APP=pbshm` and `FLASK_DEBUG=1` (Only for Windows and Linux operating systems).