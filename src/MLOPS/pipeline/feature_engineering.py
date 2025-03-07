from src.MLOPS import logger
from src.MLOPS.components.feature_engineering import feature_engineering_components
from src.MLOPS.utils.common import read_yaml,file_creation
from src.MLOPS.constants import *
from src.MLOPS.configurations.configurations import config_manager
import pandas as pd



class feature_engineering_pipeline:
    def feature_engineering():
        data_path,train_path,test_path=config_manager.feature_eng_config()

        data=pd.read_csv(data_path)
        feature_eng=feature_engineering_components
        feature_eng.data_splitting_saving(data,train_path,test_path)
