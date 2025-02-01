from src.MLOPS import logger
from src.MLOPS.utils.common import col_delete,del_data_greater


class Data_transformation:
    #call this function to delete the data
    def del_data_greater(col_name,data,value):
        data = data[data[col_name] <= value]
        return data

    def del_data_lesser(col_name,data,value):
        data = data[data[col_name] >= value]
        return data

    def col_delete(col_name,data):
        data=data.drop(columns=[col_name],axis=1)
        return data