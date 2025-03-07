from src.MLOPS import logger
from sklearn.model_selection import train_test_split
from src.MLOPS.utils.common import save_transformed_data

class feature_engineering_components:


    def data_splitting_saving(data,train_filepath,test_filepath):
        
        train,test=train_test_split(data,test_size=0.2)
        save_transformed_data(train,train_filepath)
        save_transformed_data(test,test_filepath)   


    def data_label_encoding(data):
        pass


        



