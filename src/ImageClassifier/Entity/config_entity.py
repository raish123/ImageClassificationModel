import os,sys
from dataclasses import dataclass
from pathlib import Path


#update the entity-->means we r defining the class variable --and taking a return function to another class
@dataclass
class DataIngestionConfig():
    #definging the class variable and its rtn dtype
    source_url: str
    local_data_path: Path
    root_dir:Path
    unzip_dir:Path


#Entity for Prepare Base Model
#entity file is nothing but we r defining the parameters as class variable
#which i was used in yaml file along with it type of parameter
@dataclass
class PrepareBaseModelConfig():
    #defining the class variable init which was used in yaml file
    root_dir_path:Path
    base_model_path:Path
    update_base_model_path:Path
    include_top:bool
    weights:str
    input_shape:list
    classes:int
    batch_size:int
    epochs:int
    learning_rate:float


#Entity for Callback_model
#in these entity file we r defining the parameter which is used in yaml file as class variable
@dataclass
class CallBackModelConfig():
    # define the parameters
    root_dir_path:Path
    tensorboard_log_dir_path:Path
    model_checkpoint_path:Path


#Entity For Training Model
#updating the Entity file is nothing but parameter 
#which is used in yaml file we r defining as a class variable
@dataclass
class TrainingModelConfig():
    root_dir_path:Path
    trained_model_path:Path
    update_base_model_path:Path
    training_data_dir:Path #taking value from previous entity
    include_top:bool
    weights:str
    input_shape:list
    classes:int
    batch_size:int
    epochs:int
    augmentation:bool


@dataclass
class EvaluatingModelConfig():
    trained_model_path:Path
    training_data_dir:Path #path where image dataset contain
    all_param:dict
    batch_size:int
    input_shape:list
