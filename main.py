from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline




STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx====================x")
except Exception as e:
    logger.error(f"Error occurred during stage {STAGE_NAME}: {str(e)}")
    raise e



STAGE_NAME = "Model Validation Stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx====================x")
    
except Exception as e:
    logger.error(f"Error occurred during stage {STAGE_NAME}: {str(e)}")
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    # Add your code here
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n""x====================x")

except Exception as e:
    logger.error(f"Error occurred during stage {STAGE_NAME}: {str(e)}")
    raise e

STAGE_NAME = "Model Triner Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    # Add your code here
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.initiate_model_training()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx====================x")
except Exception as e:
    logger.error(f"Error occurred during stage {STAGE_NAME}: {str(e)}")
    raise e





