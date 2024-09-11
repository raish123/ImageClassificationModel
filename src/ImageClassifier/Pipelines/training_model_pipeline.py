from src.ImageClassifier.Config import ConfigurationManager
from src.ImageClassifier.Exception import CustomException
from src.ImageClassifier.loggers import logger
from src.ImageClassifier.Components.training_model import TrainingModel
from src.ImageClassifier.Components.Callbacks_model import CallBackModel
import os,sys


class TrainingModelPipeline():
    def __init__(self):
        pass

    def main(self):
        try:
            #creating an object of ConfigurationManager class
            cm = ConfigurationManager()

            #calling the method of class
            call_back_config = cm.get_callback_config()

            #calling the method to get training config from configurationmanager class
            train_config = cm.get_training_config()

            #creating an object of callbacks class
            cb = CallBackModel(config=call_back_config)

            #calling teh mthod of callbacks class
            lst_obj = cb.callback()

            #creating an object of TrainingModel
            tm = TrainingModel(config=train_config)

            #calling the method of TrainingModel class
            tm.load_sequential_model()

            #calling the valid generato method
            tm.train_valid_generator()

            tm.train(callback_list=lst_obj)

        except Exception as e:
            raise CustomException(e,sys)

