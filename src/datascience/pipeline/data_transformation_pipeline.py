from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTranformation
from src.datascience import logger
from pathlib import Path

STAGE_NAME = 'Data Tranformation Stage'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        
        try:
            with open(Path("D:\\Udemy\\ML_Bootcamp\\18_End_to_End_DataScience_Project\\datascienceproject\\artifacts\\data_validation\\status.txt"),'r') as f:
                status= f.read().split(" ")[-1]
            if status=="True":
                logger.info(f"{STAGE_NAME} initiated.")
                
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTranformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                logger.info(f"{STAGE_NAME} skipped due to data validation stage failure.")
                raise Exception("Your data schema is not valid")
        except Exception as e:
            logger.error(f"Error occurred during {STAGE_NAME}: {str(e)}")
            raise e



























