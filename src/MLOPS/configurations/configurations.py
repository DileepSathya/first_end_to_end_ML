from src.MLOPS import logger
from src.MLOPS.utils.common import read_yaml,file_creation
from src.MLOPS.constants import *

class config_manager:
    def data_ingestion_config():
        yaml_file=read_yaml(CONFIG_FILE_PATH)
        file_path=yaml_file["data_ingestion"]["location"]
        data_url=yaml_file["data_ingestion"]["url"]
        unzip_path=yaml_file["data_ingestion"]["unzip_loc"]
        logger.info("reading yamlfile successful i data_ingestion")

        return data_url,file_path,unzip_path

    def data_transformation_config():
        yaml_file=read_yaml(CONFIG_FILE_PATH)
        to_del_1=yaml_file['data_transformation']['to_del']
        to_del_row_1=yaml_file['data_transformation']['to_modify_1']
        to_del_row_2=yaml_file['data_transformation']['to_modify_2']
        thrs_value_age=yaml_file['data_transformation']['threshold_value_age']
        thrs_value_exp=yaml_file['data_transformation']['threshold_value_exp']
        logger.info("reading yamlfile successful in data_transformation")
        
        return to_del_1,to_del_row_1,to_del_row_2,thrs_value_age,thrs_value_exp



if __name__=="__main__":
    
    config_manager.data_ingestion_config()