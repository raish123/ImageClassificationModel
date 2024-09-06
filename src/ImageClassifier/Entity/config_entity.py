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