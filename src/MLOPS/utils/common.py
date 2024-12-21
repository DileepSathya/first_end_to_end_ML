import os
from src.MLOPS import logger
import yaml
from pathlib import Path

def file_creation(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            logger.info(f"Created missing directory: {directory}")
        except Exception as e:
            logger.error(f"Failed to create directory: {directory}. Error: {e}")

# Check if the file exists
    if os.path.exists(path):
        try:
            # Open the file for reading
            with open(path, "r") as f:
                contents = f.read()
                print(contents)
                logger.info("File is present. Contents displayed.")
        except Exception as e:
            logger.error(f"An error occurred while reading the file: {e}")
    else:
        try:
            # Create the file if it doesn't exist
            with open(path, "x") as f:
                pass
            logger.info("File not found. Created an empty file.")
        except Exception as e:
            logger.error(f"An error occurred while creating the file: {e}")

def read_yaml(yaml_path):
    try:
        with open(yaml_path) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file{yaml_path} loaded succesfully")
            return content
    except Exception as e:
        raise e

       
if __name__=="__main__":
    read_yaml(Path("config/config.yaml"))
    