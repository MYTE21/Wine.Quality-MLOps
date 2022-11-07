import os

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebook",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as d:
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    os.path.join("src", "__init__.py"),
]

for file_ in files:
    with open(file_, "w") as f:
        pass
