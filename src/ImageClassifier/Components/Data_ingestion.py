from src.ImageClassifier.Exception import CustomException
from src.ImageClassifier.loggers import logger
from src.ImageClassifier.Entity import DataIngestionConfig
from src.ImageClassifier.Utils import download_data_from_s3,read_yaml_file,Create_Directory

#updating the components file!!!
class DataIngestion():
    #constructor method to initialize the dataingestionconfig class init!!!
    def __init__(self,config:DataIngestionConfig):
        self.config = config #rtn parameter value init which was define

        self.source_url = self.config.source_url
        self.local_data_path = self.config.local_data_path
        self.unzip_dir = self.config.unzip_dir


        #calling the function download data from s3 Bucket
        download_data_from_s3(local_data_file=self.local_data_path)


    