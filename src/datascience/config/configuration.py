from src.datascience.constants import *
from src.datascience.utils.common import read_yaml,create_dictionaries
from src.datascience.entity.config_entity import (DataIngestionconfig,DataValidationConfig,DataTransformationConfig,ModelTrainingConfig,ModelEvaluationConfig)
import os 

os.environ["MLFLOW_TRACKING_URL"] ="https://dagshub.com/surani.mayur/datascienceproject.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="surani.mayur"
os.environ["MLFLOW_TRACKING_PASSWORD"]="XXXXXXXXXXXXXXXXXXXXXXXXXXXX"

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


    def get_model_trainer_config(self) -> ModelTrainingConfig:
        config=self.config.model_trainer
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN
        
        create_dictionaries([config.root_dir])
        
        model_trainer_config= ModelTrainingConfig(
            root_dir=Path(config.root_dir),
            train_data_path=Path(config.train_data_path),
            test_data_path=Path(config.test_data_path),
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name,
        )
        
        return model_trainer_config
        
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        
        create_dictionaries([config.root_dir])
        
        model_evaluation_config=ModelEvaluationConfig(
            root_dir=(config.root_dir),
            test_data_path=(config.test_data_path),
            model_path=(config.model_path),
            all_params=self.params,
            metric_file_name=(config.metric_file_name),
            target_column=schema.name,
            mlflow_uri='https://dagshub.com/surani.mayur/datascienceproject.mlflow'     #os.environ["MLFLOW_TRACKING_URL"]  # Using environment variable for mlflow URI
        )
        
        return model_evaluation_config