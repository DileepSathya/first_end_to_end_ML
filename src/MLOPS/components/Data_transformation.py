from src.MLOPS import logger
from src.MLOPS.utils.common import col_delete,del_data_greater,file_creation



class Data_transformation:
    #call this function to delete the data
    def del_data_lesser(col_name,data,value):
        data = data[data[col_name] <= int(value)]
        return data

    def del_data_greater(col_name,data,value):
        data = data[data[col_name] >= value]
        return data

    def col_delete(col_name,data):
        data=data.drop(columns=[col_name],axis=1)
        return data
    def save_transformed_data(data, file_path):
        
        file_creation(file_path)
        data.to_csv(file_path, index=False)  # Assuming data is a DataFrame
        print(f"Transformed data saved to {file_path}")