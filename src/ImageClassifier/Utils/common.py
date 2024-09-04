#Utils Provide Functionality To Enitre Application!!
import os,sys
from src.ImageClassifier.loggers import logger
from src.ImageClassifier.Exception import CustomException
import boto3
from dotenv import load_dotenv
from pathlib import Path
import yaml
from ensure import ensure_annotations
import joblib
import json
import dill
from box import ConfigBox
from typing import Any

load_dotenv()  # take environment variables from .env. 
secret_key = os.getenv(key="Secret_access_key")
access_key = os.getenv(key = "Access_key_ID")
region = os.getenv(key = "Region")

#creating Function to download Data from AWS-S3 Bucket
@ensure_annotations
def download_data_from_s3(local_data_file):
    global secret_key,access_key,region
    try:
        s3 = boto3.resource("s3")

        #now creating low level to connect to client Bucket
        client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region,
            verify = False
            
        )

        object_key='Data.zip'
        bucket_name='raishmumbaibucket'

        # Local path for the downloaded ZIP file
        local_zip_path = os.path.join(local_data_file, os.path.basename(object_key)) #we take it from yaml files

        with open(local_zip_path,"wb") as file_obj:
            client.download_file(bucket_name,object_key,file_obj)

        logger.info(f"File Downloaded to Local_date_file {local_data_file}")
    except Exception as e:
        raise CustomException(e,sys)
    

#creating a function to read the yaml file--->rtn result to ConfigBox Dict
@ensure_annotations
def read_yaml_file(filepath: Path) -> ConfigBox:
    try:
        logger.info(f'Reading the YAML file {filepath}')
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)
            logger.info(f'YAML file read successfully: {filepath}')
            return ConfigBox(data)

    except Exception as e:
        raise CustomException(e, sys)
    

#Creating a Function to Create Directories
@ensure_annotations
def Create_Directory(path_to_directories:list,verbose=True):
    try:
        logger.info(f'Creating Directory')
        for filepath in path_to_directories:
            if not os.path.exists(filepath):
                os.makedirs(filepath,exists_ok=True)
                logger.info(f'Directory Created at {filepath}')
    except Exception as e:
        raise CustomException(e,sys)


#Creating Function TO Save Object File
@ensure_annotations
def Save_Object(filepath:Path,Obj):
    try:
        logger.info(f'Saving Object File {filepath}')
        if not os.path.exists('artifacts'):
            os.makedirs('artifacts')
        with open(filepath,'wb') as file:
            dill.dump(Obj,file)
        logger.info('Object Save to Directory')
    except Exception as e:
        raise CustomException(e,sys)

#Creating Function to read json file
@ensure_annotations
def read_json_file(filepath: Path) -> ConfigBox:
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return ConfigBox(data)
    except Exception as e:
        raise CustomException(e, sys)
    
#Creating Function to write json file
@ensure_annotations
def write_json_file(filepath: Path, data: dict):
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            print(f"Data successfully written to {filepath}")
    except Exception as e:
        raise CustomException(e,sys)
    
#Creating Function to Save Binary File!!
@ensure_annotations
def Save_Binary_File(filepath: Path,data: Any):
    try:
        
        joblib.dump(value=data,filename=filepath)

    except Exception as e:
        raise CustomException(e,sys)
    
#Creating Function to Load Binary File!!
@ensure_annotations
def Load_Binary_File(filepath: Path) -> Any:
    try:
        data = joblib.load(filename=filepath)
        return data

    except Exception as e:
        raise CustomException(e,sys)