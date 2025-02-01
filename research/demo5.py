from src.MLOPS import logger
from src.MLOPS.utils.common import read_yaml,file_creation
from src.MLOPS.constants import *
def data_transformation_config():
        yaml_file=read_yaml(CONFIG_FILE_PATH)
        to_del_1=yaml_file['data_transformation']['to_del']
        to_del_row_1=yaml_file['data_transformation']['to_modify_1']
        to_del_row_2=yaml_file['data_transformation']['to_modify_2']
        print(to_del_1,to_del_row_1,to_del_row_2)
data_transformation_config()


