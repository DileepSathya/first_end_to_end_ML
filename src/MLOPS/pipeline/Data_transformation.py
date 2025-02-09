'''data transformation pipeline
    load data from config.yaml file
    send it to the componenets.data_transformation
'''
from src.MLOPS import logger
from src.MLOPS.components.Data_transformation import Data_transformation
from src.MLOPS.utils.common import read_yaml,file_creation
from src.MLOPS.constants import *
from src.MLOPS.configurations.configurations import config_manager
import pandas as pd



        
class DataTransformationPipeline:
    def data_transformation():
        
        name_col_del,row_del_emp,row_del_age,age_thrs,exp_thrs,data,transformed_file_path=config_manager.data_transformation_config()
        
        data=pd.read_csv(data)
        data=Data_transformation.del_data_lesser(row_del_emp,data,exp_thrs)
        data=Data_transformation.del_data_lesser(row_del_age,data,age_thrs)
        data=Data_transformation.col_delete(name_col_del,data)
        Data_transformation.save_transformed_data(data, transformed_file_path)