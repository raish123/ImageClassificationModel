#This Module we used to create Project Structure
import sys,os
from pathlib import Path #this class auomatically change the filepath to windows,Mac,Linux path
from datetime import datetime
import logging #this module we used to track the error and generate text logs in it

project_name = "ImageClassifier"

FORMAT = "[%(asctime)s]-%(levelname)s-%(lineno)d-%(message)s"

#configuraing the logging module
logging.basicConfig(
    filename = f"{project_name}.log",
    filemode='w',
    format = FORMAT,
    level= logging.INFO,
)

#creating a list of file and directories want in this project Structure
lst_files = [
    ".github/workflows/.gitkeep",
    "config/config.yaml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/Exception.py",
    f"src/{project_name}/loggers.py",
    f"src/{project_name}/Components/__init__.py",
    f"src/{project_name}/Components/Data_ingestion.py",
    f"src/{project_name}/Utils/__init__.py",
    f"src/{project_name}/Utils/common.py",
    f"src/{project_name}/Entity/__init__.py",
    f"src/{project_name}/Constants/__init__.py",
    f"src/{project_name}/Config/__init__.py",
    f"src/{project_name}/Config/configuration.py",
    f"src/{project_name}/Pipelines/__init__.py",
    "params.yaml",
    "requirements.txt",
    "Dockerfile",
    "Makefile",
    "research/trials.ipynb",
    "main.py",
    "setup.py",
    "templates/index.html",
    "test.py"
]

#iterating each element from list and creating directories
for filepath in lst_files:
    #changing the filepath to windows path
    filepath = Path(filepath)

    #splitting the filepath
    dirpath, filename = os.path.split(filepath)

    #now checking dirpath is exist or not it should be empty
    if dirpath!= "":
        #if not exist then creating the directory
        os.makedirs(dirpath, exist_ok=True)
        logging.info(f"directory cretaed {dirpath} for filename {filename}")

    #creating files in directory exist or not also checking the size of fileapth is zero
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        #if not exist then creating the file
        with open(filepath,"wb") as file:
            pass
            logging.info(f"filepath created zero size {filepath}")
    else:
        logging.info(f"Filepath already Exist {filepath}")
