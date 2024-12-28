from src.MLOPS import logger
from src.MLOPS.utils.common import read_yaml,file_creation
from src.MLOPS.constants import *

class config_manager:
    def data_ingestion_config():
        yaml_file=read_yaml(CONFIG_FILE_PATH)
        file_path=yaml_file["data_ingestion"]["location"]
        data_url=yaml_file["data_ingestion"]["url"]
        unzip_path=yaml_file["data_ingestion"]["unzip_loc"]
        logger.info("reading yamlfile successful")

        return data_url,file_path,unzip_path






if __name__=="__main__":
    
    config_manager.data_ingestion_config()