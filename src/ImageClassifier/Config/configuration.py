from src.ImageClassifier.Utils import download_data_from_s3,read_yaml_file,Create_Directory
from src.ImageClassifier.Constants import *
from src.ImageClassifier.Exception import CustomException
from src.ImageClassifier.loggers import logger
from src.ImageClassifier.Entity import DataIngestionConfig


#update the configuration manager file in src/config/conbfiguration.py
class ConfigurationManager():
    def __init__(self, config_file_path=CONFIG_FILEPATH,params_file_path=PARAM_FILEPATH):
        #reading all the yaml file 
        self.config = read_yaml_file(config_file_path) #rtn as configbox dicatonary
        self.params = read_yaml_file(params_file_path) #rtn as paramsbox dictionary

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