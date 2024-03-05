import sys
import os
import subprocess
import pathlib
import venv

parent_dir = pathlib.Path(os.getcwd()).parent.resolve()
venv_name = "env"  # Could pass this as a param in cookiecutter.json.
env_path = str(parent_dir / venv_name)

python_executable = sys.executable  # Use current interpreter. 

subprocess_params = {
    "stdout": subprocess.PIPE,
    "stderr": subprocess.PIPE,
    "check": True
}

try:
    # Create the venv, could modify the python version here.
    venv.create(env_path, with_pip=True)

    # Determine the path to the venv's python executable
    if sys.platform == "win32":
        venv_python = os.path.join(env_path, "Scripts", "python.exe")
        
        # Adding environment variables to environment activation.
        env_vars_cmd = [
            "set FLASK_APP=pbshm",
            "set FLASK_DEBUG=1"
        ]
        with open(os.path.join(env_path, "Scripts", "activate.bat"), 'a') as file:
            file.write("\r\n" + "\r\n".join(env_vars_cmd))
    
        env_vars_ps = [
            "$env:FLASK_APP = 'pbshm'",
            "$env:FLASK_DEBUG = '1'"
        ]
        with open(os.path.join(env_path, "Scripts", "Activate.ps1"), 'a') as file:
            file.write('\n' + '\n'.join(env_vars_ps))

    elif sys.platform in ("linux", "linux2"):
        venv_python = os.path.join(env_path, "bin", "python")
        env_vars_linux = [
            "export FLASK_APP=pbshm",
            "export FLASK_DEBUG=1"
        ]
        with open(os.path.join(venv_python, "bin", "activate"), 'a') as file:
            file.write('\n' + '\n'.join(env_vars_linux))
    
    else:
        raise OSError("Unsupported operating system. Currently only Linux and Windows are supported.")

    # Install pbshm core/framework in venv by directly using the venv's python executable
    print("Installing PBSHM", "{{ cookiecutter.project_type }}".title())
    result = subprocess.run([venv_python, "-m", "pip", "install", "pbshm-{{ cookiecutter.project_type }}"], **subprocess_params)
    
    print(f"stdout pip install pbshm-core: {result.stdout.decode()}")
    print(f"stderr pip install pbshm-core: {result.stderr.decode()}")

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e.output.decode()}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
