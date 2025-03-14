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
        data =yaml_file['data_transformation']['data_path']
        to_del_1=yaml_file['data_transformation']['to_del']
        to_del_row_emp=yaml_file['data_transformation']['to_modify_exp']
        to_del_row_age=yaml_file['data_transformation']['to_modify_age']
        thrs_value_age=int(yaml_file['data_transformation']['threshold_value_age'])
        thrs_value_exp=int(yaml_file['data_transformation']['threshold_value_exp'])
        transformed_file_path=yaml_file['data_transformation']['transformed_file_path']

        logger.info("reading yamlfile successful in data_transformation")
        
        return to_del_1,to_del_row_emp,to_del_row_age,thrs_value_age,thrs_value_exp,data,transformed_file_path


    def feature_eng_config():
        yaml_file=read_yaml(CONFIG_FILE_PATH)

        data_path=yaml_file['feature_engineering']['data_path']
        train_path=yaml_file['feature_engineering']['train_filepath']
        test_path=yaml_file['feature_engineering']['test_filepath']
        le_path=yaml_file['feature_engineering']['LE_yaml_path']
        scaled_train_path=yaml_file['feature_engineering']['scaled_train_data_path']
        scaled_test_path=yaml_file['feature_engineering']['scaled_test_data_path']
        final_train_path=yaml_file['feature_engineering']['final_train_path']
        final_test_path=yaml_file['feature_engineering']['final_test_path']

        logger.info("reading yamlfile successful in feature_engineering")

        return data_path,train_path,test_path,le_path,scaled_train_path,scaled_test_path,final_train_path,final_test_path
if __name__=="__main__":
    
    config_manager.data_ingestion_config()