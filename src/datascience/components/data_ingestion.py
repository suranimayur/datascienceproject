import os 
import urllib.request as request
from src.datascience import logger
import zipfile

from src.datascience.entity.config_entity import (DataIngestionconfig)

## component Data Ingestion

class DataIngestion:
    def __init__(self, config: DataIngestionconfig):
        self.config = config
    
    # Downloading the zip file
      
    def download_file(self):
        if os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file,
            )
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists.")
    
    # Unzipping the downloaded file
    
    def extract_zip_file(self):
        """
        zip_file_path: str 
        Extract the zip file into the data directory
        
        Function returns None
        
        """
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Zip file {self.config.local_data_file} extracted to {unzip_path}.")













