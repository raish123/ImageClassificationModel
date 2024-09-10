from src.ImageClassifier.Exception import CustomException
from src.ImageClassifier.loggers import logger
from src.ImageClassifier.Entity import CallBackModelConfig
import os,sys,tensorflow
from pathlib import Path
from src.ImageClassifier.Utils import Save_Model,read_yaml_file,Create_Directory
from datetime import datetime


#in component file we gonna initialize object to CallBackModelConfig class 
#and accessing all the parameter and value init

class CallBackModel():
    def __init__(self,config:CallBackModelConfig):
        self.config = config


    #create method to get tensorboard log directory
    @property
    def _get_tensorboard_log_dir(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

        tensorboard_log_dir = os.path.join(self.config.tensorboard_log_dir_path,f"TB_{timestamp}.log")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(tensorboard_log_dir), exist_ok=True)

        tb_directory = tensorflow.keras.callbacks.TensorBoard(
            log_dir=tensorboard_log_dir
        )
        return tb_directory
    
    #method to create model_checkpoint to save best model file after training done
    @property
    def _get_checkpont_model(self):
        checkpoint_model = tensorflow.keras.callbacks.ModelCheckpoint(
            filepath=self.config.model_checkpoint_path,
            verbose=1,
            save_best_only=True
        )
        return checkpoint_model



    def callback(self):
        return[
        self._get_tensorboard_log_dir,
        self._get_checkpont_model
        ]