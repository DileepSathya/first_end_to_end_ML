from src.MLOPS import logger
from src.MLOPS.components.Data_ingestion import Data_ingestion
from src.MLOPS.utils.common import read_yaml,file_creation
from src.MLOPS.constants import *
from src.MLOPS.configurations.configurations import config_manager

class data_ingestion_pipeline:
    def data_ingestion():
        data_url,file_path,unzip_path=config_manager.data_ingestion_config()

        file_creation(file_path)
        
        Data_ingestion.download_data(data_url,file_path)
        logger.info("downloading data from url success")
        Data_ingestion.data_unzipping(file_path,unzip_path)
        logger.info("unzipping the data successful")





if __name__=="__main__":
    data_ingestion_pipeline.data_ingestion()
