from src.ImageClassifier.Pipelines.data_ingestion_training_pipeline import TrainingPipeline
from src.ImageClassifier.loggers import logger
import os,sys
from src.ImageClassifier.Exception import CustomException


stage_name = 'Data Ingestion Stage'

try:
    logger.info(f">>> stage {stage_name} started <<<")

    tp = TrainingPipeline()
    tp.main()

    logger.info(f">>> stage {stage_name} stopped <<<")


except Exception as e:
    raise CustomException(e,sys)