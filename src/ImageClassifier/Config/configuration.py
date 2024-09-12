from src.ImageClassifier.Utils import download_data_from_s3,read_yaml_file,Create_Directory
from src.ImageClassifier.Constants import *
from src.ImageClassifier.Exception import CustomException
from src.ImageClassifier.loggers import logger
from src.ImageClassifier.Entity import DataIngestionConfig,CallBackModelConfig,PrepareBaseModelConfig,TrainingModelConfig,EvaluatingModelConfig


#update the configuration manager file in src/config/conbfiguration.py
class ConfigurationManager():
    def __init__(self, config_file_path=CONFIG_FILEPATH,param_file_path=PARAM_FILEPATH):
        #reading all the yaml file 
        self.config = read_yaml_file(config_file_path) #rtn as configbox dicatonary
        self.param = read_yaml_file(param_file_path) #rtn as paramsbox dictionary

        #creating artifacts main directory through uitls fiunction
        Create_Directory([self.config.artifacts_root]) #it will create directory artifacts in project structure
        logger.info(f'Config Filepath {self.config} root directory Created Artifacts')
    
    #creating another instance method to initialize the value to class variable of DataIngestionConfig from config.yaml se
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        self.config = self.config.dataingestion #rtn as configbox dicatonary
        logger.info(f"get data ingestion config instance method value {self.config}")

        #creating an object of DataIngestionConfig and initialize the class variable as value init
        data_ingestion_config = DataIngestionConfig(
            source_url=self.config.source_url,
            local_data_path = self.config.local_data_file,
            root_dir=self.config.root_dir,
            unzip_dir=self.config.unzip_dir
        )

        return data_ingestion_config
    
    #creating another method to initialize the value to the PrepareBaseModelConfig class variable to it and taking rtn as function
    def get_base_model_config(self) ->PrepareBaseModelConfig:
        self.config = self.config.prepare_base_model # rtn as configbox dictatonary

        #creating root directory for prepare_base_model key of yaml file
        Create_Directory([self.config.root_dir_path]) #artifacts/base_model directory created in project structure

        #now initializing the class variable value by creating an object PrepareBaseModelConfig class!!
        base_model_config = PrepareBaseModelConfig(
            root_dir_path=self.config.root_dir_path,
            base_model_path=self.config.base_model_path,
            update_base_model_path=self.config.update_base_model_path,
            include_top=self.param.include_top,
            weights=self.param.weights,
            input_shape=self.param.input_shape,
            classes=self.param.classes,
            batch_size=self.param.batch_size,
            epochs=self.param.epochs,
            learning_rate=self.param.learning_rate
        )

        return base_model_config
    
    #now initialize the class variable value to it-->for which we are creating method
    def get_callback_config(self) -> CallBackModelConfig:
        try:
            # Accessing the prepare_callback_model section of the config
            callback_config = self.config.prepare_callback_model

            # Creating necessary directories for callback artifacts
            chkpt_directory = os.path.dirname(callback_config.model_checkpoint_path)
            Create_Directory([callback_config.root_dir_path, chkpt_directory])

            # Creating and returning the CallBackModelConfig object
            call_back_config =  CallBackModelConfig(
                root_dir_path=callback_config.root_dir_path,
                tensorboard_log_dir_path=callback_config.tensorboard_log_dir_path,
                model_checkpoint_path=callback_config.model_checkpoint_path
            )
            return call_back_config

        except KeyError as e:
            raise CustomException(f"KeyError in callback config: {e}", sys)
        except Exception as e:
            raise CustomException(f"An error occurred in callback config: {e}", sys)
    

    # Method to initialize the training configuration and return the TrainingModelConfig object
    def get_training_config(self) -> TrainingModelConfig:
        try:
            # Accessing the prepare_training section of the config
            training_config = self.config.prepare_training

            # Creating the necessary directories for training artifacts
            Create_Directory([training_config.root_dir_path])

            # Creating and returning the TrainingModelConfig object
            return TrainingModelConfig(
                root_dir_path=training_config.root_dir_path,
                trained_model_path=training_config.trained_model_path,
                update_base_model_path=self.config.prepare_base_model.update_base_model_path,
                include_top=self.param.include_top,
                weights=self.param.weights,
                input_shape=self.param.input_shape,
                classes=self.param.classes,
                batch_size=self.param.batch_size,
                epochs=self.param.epochs,
                training_data_dir=training_config.training_data_dir,
                augmentation=self.param.augmentation
            )

        except KeyError as e:
            raise CustomException(f"KeyError in training config: {e}", sys)
        except Exception as e:
            raise CustomException(f"An error occurred in training config: {e}", sys)
        
    def get_evaluation_config(self) ->EvaluatingModelConfig:
        #local variable
        eval = self.config.prepare_training

        #creating an object of EvaluatingModelConfig class
        eval_model_config = EvaluatingModelConfig(
            trained_model_path=eval.trained_model_path,
            training_data_dir=eval.training_data_dir,
            all_param=self.param,
            batch_size=self.param.batch_size,
            input_shape=self.param.input_shape
        )
        return eval_model_config
