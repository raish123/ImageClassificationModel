from src.ImageClassifier.Config import ConfigurationManager
from src.ImageClassifier.Exception import CustomException
from src.ImageClassifier.loggers import logger
import os,sys
from src.ImageClassifier.Components.Callbacks_model import CallBackModel


class CallbackModelTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        try:
            #creating an object of ConfigurationManager class
            cm = ConfigurationManager()

            #calling the method of class
            call_back_config = cm.get_callback_config()

            #creating an object of callbacks class
            cb = CallBackModel(config=call_back_config)

            #calling teh mthod of callbacks class
            lst_obj = cb.callback()

            logger.info(lst_obj)

        except Exception as e:
            raise CustomException(e,sys)
