import os
from src.MLOPS import logger
import yaml
from pathlib import Path

def file_creation(filepath):
    
# Check if the file exists
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logger.info(f"Creating directory {filedir} for the file : {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:

            pass
            logger.info(f"Creating empty file: {filepath}")

    else:
        logger.info(f"{filename} is already exists")

def read_yaml(yaml_path):
 
    try:
        with open(yaml_path) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file{yaml_path} loaded succesfully")
            return content
    except Exception as e:
        raise e
#call this function to delete the data
def del_data_greater(col_name,data,value):
    data = data[data[col_name] <= value]
    return data

def del_data_lesser(col_name,data,value):
    data = data[data[col_name] >= value]
    return data

def col_delete(col_name,data):
    data=data.drop(columns=[col_name],axis=1)
    return data


       

    
    