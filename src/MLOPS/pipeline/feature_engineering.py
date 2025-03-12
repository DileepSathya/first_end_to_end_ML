from src.MLOPS import logger
from src.MLOPS.components.feature_engineering import feature_engineering_components
from src.MLOPS.utils.common import read_yaml,file_creation
from src.MLOPS.constants import *
from src.MLOPS.configurations.configurations import config_manager
import pandas as pd


data_path,train_path,test_path,le_yaml,scaled_train_path,scaled_test_path,final_train_path,final_test_path=config_manager.feature_eng_config()
class feature_engineering_pipeline:
    
    def feature_engineering():
        

        data=pd.read_csv(data_path)
        feature_eng=feature_engineering_components
        feature_eng.data_splitting_saving(data,train_path,test_path,False)
        logger.info("entering data lebleing phase")
        x_train,x_test=feature_eng.data_label_encoding(train_path,test_path,le_yaml)
        logger.info("done data lebleing phase")
        train=pd.read_csv(train_path)
        scaled_train_data=feature_eng.train_data_scaling(train,x_train,scaled_train_path)
        logger.info("done train data scaling ")

        test=pd.read_csv(test_path)
        scaled_test_data=feature_eng.train_data_scaling(test,x_test,scaled_test_path)
        logger.info("done test data scaling ")

        final_combined_df=feature_eng.data_combinig_shuffling_splitting(scaled_train_data,scaled_test_data)

        logger.info("combined scaled test and train data to shufflee them")
        feature_eng.data_splitting_saving(final_combined_df,final_train_path,final_test_path,True)

        logger.info("final train and test data ready shuffled")




    

        

        
        