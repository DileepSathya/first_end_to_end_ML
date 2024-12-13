import os
from src.MLOPS import logger



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
       
if __name__=="__main__":
    file_creation("params/params.yaml")