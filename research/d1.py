"""import urllib.request as request
from src.MLOPS import logger
def download_data():
    filename,headers=request.urlretrieve(
        url="https://www.kaggle.com/api/v1/datasets/download/vedaantsingh/loan-application-risk-prediction-data",
        filename="artifacts/data_ingestion/data.zip"
    )
if __name__=="__main__":
    download_data()
"""

"""from src.MLOPS.utils.common import file_creation
filename="artifacts/data_ingestion/data.zip"
filename2="artifacts/data_validation/data.zip"
file_creation(filename)
file_creation(filename2)"""

"""from src.MLOPS.utils.common import read_yaml,file_creation
from src.MLOPS.constants import *

x=read_yaml(CONFIG_FILE_PATH)
#y=x.data_ingestion
print(x["data_ingestion"]["data_download_path"])"""

"""import zipfile
from src.MLOPS.utils.common import file_creation
filepath="artifacts/data_ingestion/data.zip"
unzip_save="artifacts/data_ingestion/data"
def data_unzipping():
    with zipfile.ZipFile(filepath,'r') as zipref:
        zipref.extractall(unzip_save)
    

data_unzipping()"""
