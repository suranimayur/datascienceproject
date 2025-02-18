from src.datascience.constants import *
from src.datascience.utils.common import read_yaml,create_dictionaries
from src.datascience.entity.config_entity import (DataIngestionconfig,DataValidationConfig,DataTransformationConfig)

class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH
                 ):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)
        
        create_dictionaries([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionconfig:
        config= self.config.data_ingestion
        create_dictionaries([config.root_dir])        
        
        data_ingestion_config = DataIngestionconfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )
        return data_ingestion_config
               

    def get_data_validation_config(self) -> DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema.COLUMNS
        create_dictionaries([config.root_dir])        
        
        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=Path(config.unzip_data_dir),
            all_schema=schema
          
        )
        return data_validation_config   
    

        
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config= self.config.data_transformation
        create_dictionaries([config.root_dir])        
        
        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path)
        )
        return data_transformation_config 



