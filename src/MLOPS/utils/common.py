import os
from src.MLOPS import logger
import yaml
from pathlib import Path
def file_creation(filepath):
    filepath = Path(filepath)
    filedir, filename = filepath.parent, filepath.name

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logger.info(f"Creating directory {filedir} for the file: {filename}")
    
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
        logger.info(f"Creating empty file: {filepath}")
    else:
        logger.info(f"{filename} already exists")

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


       


def save_transformed_data(data, file_path):
    file_creation(file_path)
    data.to_csv(file_path, index=False)  # Assuming data is a DataFrame
    print(f"Transformed data saved to {file_path}")

def dict_to_yaml(data_dict,le_yaml_filepath):
    with open(le_yaml_filepath, 'w') as outfile:
        yaml.dump(data_dict, outfile, default_flow_style=False)
    