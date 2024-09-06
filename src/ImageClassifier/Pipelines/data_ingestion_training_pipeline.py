from src.ImageClassifier.Config import ConfigurationManager
from src.ImageClassifier.Exception import CustomException
from src.ImageClassifier.loggers import logger
from src.ImageClassifier.Components.Data_ingestion import DataIngestion
import os,sys


class TrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        #creating an object of configuration manager
        cm = ConfigurationManager()

        #getting built in method ConfigurationManager class
        data_ingestion = cm.get_data_ingestion_config()
        logger.info(data_ingestion)

        #creating an object of dataingestion class
        di = DataIngestion(config=data_ingestion)
        
