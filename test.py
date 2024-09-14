from src.ImageClassifier.Exception import CustomException
from src.ImageClassifier.loggers import logger
import os,sys

try:
    logger.info("Checking For logs")
    a = 1/0
except Exception as e:
    raise CustomException(e,sys)
