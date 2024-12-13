import os

import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
project_name="MLOPS"
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/components/Data_ingestion.py",
    f"src/{project_name}/components/Data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluater.py",
    f"src/{project_name}/pipeline/Data_ingestion.py",
    f"src/{project_name}/pipeline/Data_transformation.py",
    f"src/{project_name}/pipeline/model_trainer.py",
    f"src/{project_name}/pipeline/model_evaluater.py",

    "main.py",
    "app.py",
    "setup.py"

]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file : {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:

            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")