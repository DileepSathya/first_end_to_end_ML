from src.MLOPS import logger
from sklearn.model_selection import train_test_split
from src.MLOPS.utils.common import save_transformed_data,dict_to_yaml
import pandas as pd
class feature_engineering_components:


    def data_splitting_saving(data,train_filepath,test_filepath):
        
        train,test=train_test_split(data,test_size=0.2)
        save_transformed_data(train,train_filepath)
        save_transformed_data(test,test_filepath)   


    def data_label_encoding(tarin_filepath,test_filepath,le_filepath):
        train=pd.read_csv(tarin_filepath)
        test=pd.read_csv(test_filepath)
        x_train=train.drop(["loan_status"],axis=1)
        x_test=test.drop(["loan_status"],axis=1)
        logger.info("x_train,x_test ")
        from sklearn.preprocessing import LabelEncoder

        # Initialize a nested dictionary to store mappings for all columns
        mappings = {}

    # Identify categorical columns
        categorical_list = [col for col in x_train.columns if x_train[col].dtype == 'object']

    # Encode each categorical column
        for col in categorical_list:
            le = LabelEncoder()  # Create a new LabelEncoder for each column
            x_train[col] = le.fit_transform(x_train[col])
            x_test[col] = le.transform(x_test[col])
            mappings[col] = {v:int(k) for k, v in zip(le.transform(le.classes_), le.classes_)}
        print(mappings,le_filepath)
        logger.info("going to dicto yaml")
        
        dict_to_yaml(mappings,le_filepath)

        

        



