from src.MLOPS import logger
from sklearn.model_selection import train_test_split
from src.MLOPS.utils.common import save_transformed_data,dict_to_yaml,file_creation
import pandas as pd
class feature_engineering_components:


    def data_splitting_saving(data,train_filepath,test_filepath,shuff_status):
        
        train,test=train_test_split(data,test_size=0.2,shuffle=shuff_status)
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
        dict_to_yaml(mappings,le_filepath)
        return x_train,x_test
    def train_data_scaling(train,x_train,scaled_train_filepath):

        y_train=train["loan_status"]
        import pandas as pd
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
        scaled_train_data = scaler.fit_transform(x_train)
        scaled_train_data = pd.DataFrame(scaled_train_data, columns=x_train.columns)
        y_train = pd.DataFrame(y_train, columns=["loan_status"]) 
        combined_scaled_train_df = pd.concat([scaled_train_data, y_train], axis=1)


       

        save_transformed_data(combined_scaled_train_df,scaled_train_filepath)
        return combined_scaled_train_df
        
    def test_data_scaling(test,x_test,scaled_test_filepath):

        y_test=test["loan_status"]
        import pandas as pd
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
        scaled_test_data = scaler.fit_transform(x_test)
        scaled_test_data = pd.DataFrame(scaled_test_data, columns=x_test.columns)
        y_test = pd.DataFrame(y_test, columns=["loan_status"]) 
        combined_scaled_test_df = pd.concat([scaled_test_data, y_test], axis=1)
        save_transformed_data(combined_scaled_test_df,scaled_test_filepath)


        return combined_scaled_test_df
        

    def data_combinig_shuffling_splitting(scaled_train,scaled_test):
        df=pd.concat([scaled_train,scaled_test])
        return df
        



