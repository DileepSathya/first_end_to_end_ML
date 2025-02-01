'''data transformation pipeline
    load data from config.yaml file
    send it to the componenets.data_transformation
'''
from src.MLOPS import logger
from src.MLOPS.components.Data_transformation import Data_transformation
from src.MLOPS.utils.common import read_yaml,file_creation
from src.MLOPS.constants import *
from src.MLOPS.configurations.configurations import config_manager

class data_transformation_pipeline:
    def data_transformation():
        
        name_col_del,row_del_1,row_del_2,age_thrs,exp_thrs=config_manager.data_transformation_config()
        Data_transformation.del_data_greater(name_col_del,)
