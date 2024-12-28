from src.MLOPS import logger
from src.MLOPS.utils.common import read_yaml,file_creation
from src.MLOPS.constants import *
import urllib.request as request
import zipfile

class Data_ingestion:
    def download_data(data_url,file_path):
        filename,headers=request.urlretrieve(
            url=data_url,
            filename=file_path
        )
    def data_unzipping(filepath,unzip_loc):
        with zipfile.ZipFile(filepath,'r') as zipref:
            zipref.extractall(unzip_loc)




        
if __name__=="__main__":
    yaml_file=read_yaml(CONFIG_FILE_PATH)
    data_url=yaml_file["data_ingestion"]["url"]
    file_path=yaml_file["data_ingestion"]["location"]
    file_creation(file_path)
    Data_ingestion.download_data(data_url,file_path)
