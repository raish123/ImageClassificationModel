from src.ImageClassifier.Config import ConfigurationManager
from src.ImageClassifier.Exception import CustomException
from src.ImageClassifier.loggers import logger
from src.ImageClassifier.Components.evaluating import EvaluatingModelConfig,EvaluatingModel
import os,sys


class EvaluatingModelPipeline():
    def __init__(self):
        pass

    def main(self):
        try:
            cm = ConfigurationManager()
            eval_config = cm.get_evaluation_config()

            em = EvaluatingModel(eval=eval_config)

            em.trained_model_load()

            em._test_image_generator()

            em._evaluating_model()

            em._saving_score()


        except Exception as e:
            raise CustomException(e,sys)

