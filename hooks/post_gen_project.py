import os
import shutil
import pathlib

current_dir = pathlib.Path(os.getcwd())
parent_dir = current_dir.parent.resolve()
current_dir = current_dir.resolve()

top_most_old_path = os.path.join(current_dir, "parent_dir_contents")

for item in os.listdir(top_most_old_path):
    old_item_path = os.path.join(top_most_old_path, item)
    new_item_path = os.path.join(parent_dir, item)
    shutil.move(old_item_path, new_item_path)

shutil.rmtree(top_most_old_path)


# Rename relevant init file
os.rename("init_{{ cookiecutter.project_type }}.py", "__init__.py")

# Remove redundant init file
other_init = "framework" if "{{ cookiecutter.project_type}}" == "core" else "core"
os.remove(f"init_{other_init}.py")