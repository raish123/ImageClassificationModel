from src.ImageClassifier.Pipelines.data_ingestion_training_pipeline import DataIngestionTrainingPipeline
from src.ImageClassifier.Pipelines.basemodel_training_pipeline import BaseModelTrainingPipeline
from src.ImageClassifier.Pipelines.callback_model_training_pipeline import CallbackModelTrainingPipeline
from src.ImageClassifier.loggers import logger
import os,sys
from src.ImageClassifier.Exception import CustomException


stage_name = 'Data Ingestion Stage'

try:
    logger.info(f">>> stage {stage_name} started <<<")

    di = DataIngestionTrainingPipeline()
    di.main()

    logger.info(f">>> stage {stage_name} stopped <<<")


except Exception as e:
    raise CustomException(e,sys)

print()
logger.info('*'*100)


stage_name2 = 'Prepare Base Model Stage'

try:
    logger.info(f">>> stage {stage_name2} started <<<")

    bmtp = BaseModelTrainingPipeline()
    bmtp.main()

    logger.info(f">>> stage {stage_name2} stopped <<<")


except Exception as e:
    raise CustomException(e,sys)


print()
logger.info('*'*100)


stage_name3 = 'CallBack Model Stage'

try:
    logger.info(f">>> stage {stage_name3} started <<<")

    cbtp = CallbackModelTrainingPipeline()
    cbtp.main()

    logger.info(f">>> stage {stage_name3} stopped <<<")


except Exception as e:
    raise CustomException(e,sys)
