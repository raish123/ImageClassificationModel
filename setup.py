from setuptools import setup, find_packages
from typing import List

# Creating user-defined function to get requirements
def Get_Requirements(filepath: str) -> List[str]:
    requirement = []
    with open(filepath, 'r') as file:
        rows = file.read().split('\n')
        for row in rows:
            if '-e .' in row:
                continue
            else:
                requirement.append(row)
    return requirement

project_name = "ImageClassifierModel"

# Creating an object of the setup class from setuptools library
setup(
    name='ImageClassifierModel',
    version='0.0.0',
    long_description=open('readme.md', 'r').read(),
    author='Raees Azam Shaikh',
    author_email='shaikhraishazam@gmail.com',
    url='https://github.com/raish123/ImageClassificationModel.git',
    # Creating an object of the find_packages class from setuptools library
    packages=find_packages(),  # This class is responsible for installing all the packages present in requirements.txt
    install_requires=Get_Requirements('requirements.txt'),  # Will be a list of libraries
)
