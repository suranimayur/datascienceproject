import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import DataIngestionconfig
from typing import NoReturn

class DataIngestion:
    """
    Component responsible for data ingestion operations including downloading and extracting data files.
    """
    def __init__(self, config: DataIngestionconfig):
        """
        Initialize DataIngestion with configuration.

        Args:
            config (DataIngestionconfig): Configuration for data ingestion
        """
        self.config = config

    def download_file(self) -> NoReturn:
        """
        Downloads file from source URL if it doesn't exist locally.

        Raises:
            URLError: If download fails
            IOError: If file operations fail
        """
        try:
            if not os.path.exists(self.config.local_data_file):
                os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} downloaded! with following info: \n{headers}")
            else:
                logger.info(f"File {self.config.local_data_file} already exists.")
        except Exception as e:
            logger.error(f"Error downloading file: {str(e)}")
            raise

    def extract_zip_file(self) -> NoReturn:
        """
        Extracts the downloaded zip file to specified directory.

        Raises:
            zipfile.BadZipFile: If zip file is corrupted
            IOError: If extraction fails
        """
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)

            if not os.path.exists(self.config.local_data_file):
                raise FileNotFoundError(f"Zip file not found at {self.config.local_data_file}")

            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f"Zip file {self.config.local_data_file} extracted to {unzip_path}")
        except zipfile.BadZipFile:
            logger.error("Invalid zip file format")
            raise
        except Exception as e:
            logger.error(f"Error extracting zip file: {str(e)}")
            raise