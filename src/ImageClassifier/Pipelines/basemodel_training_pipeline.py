from src.ImageClassifier.Config import ConfigurationManager
from src.ImageClassifier.Exception import CustomException
from src.ImageClassifier.loggers import logger
import os,sys
from src.ImageClassifier.Components.Base_Model import BaseModel


class BaseModelTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        try:
            #now creating an object of configuration manager class
            cm = ConfigurationManager()

            #now calling the method to get the configuration
            base_model_config = cm.get_base_model_config()

            #creating an object of BaseModel class
            bm = BaseModel(config=base_model_config)

            #now calling the method to get the model
            bm.basemodel()

            #now calling the method to get the updated sequential model
            bm.update_base_model()
            
        except Exception as e:
            raise CustomException(e,sys)