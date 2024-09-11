from src.ImageClassifier.Exception import CustomException
from src.ImageClassifier.loggers import logger
from src.ImageClassifier.Entity import TrainingModelConfig
from src.ImageClassifier.Utils import download_data_from_s3,read_yaml_file,Create_Directory,Save_Model
import tensorflow
from datetime import datetime
from pathlib import Path


# CREATING TRAINING COMPONENT

class TrainingModel():
    def __init__(self,config:TrainingModelConfig):
        self.config = config

    #creating method for training the model first loading the sequential updated model by using model load class of tf
    def load_sequential_model(self):
        self.model = tensorflow.keras.models.load_model(
            filepath=self.config.update_base_model_path
        )

    #creating method to get train_valid_generator
    def train_valid_generator(self):
        datagenerator_kwargs = dict(
                rescale = 1./255, #normalizing the image to pixel 0 to 255
                validation_split=0.20  #testing data would be 20%
            )

        dataflow_kwargs = dict(
                target_size=self.config.input_shape[:-1], #list [224,224,3] of image se removing the channel of image
                batch_size=self.config.batch_size,
                interpolation="bilinear" # This is the method used for resizing images.
                #Bilinear interpolation is one of the options for smooth resizing.
            )

        #calling the class of tensorflow to start the preprocessing the image and generate the image data generator
        valid_datagenerator = tensorflow.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        ) 

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data_dir,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )
        #Training Data Generator with Augmentation

        if self.config.augmentation:
            train_datagenerator = tensorflow.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )

        else:
            train_datagenerator = valid_datagenerator #rtn train_datagenrator as it is without performing the augmentation

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data_dir,
            subset="training", #This loads the training data (80% of the total data).
            shuffle=True, #Training data is shuffled to prevent the model from learning the order of images rather than the content.
            **dataflow_kwargs #As with the validation generator, the image size, batch size, and interpolation method are applied here.
        )

    
    #initiate the training the model
    def train(self, callback_list: list):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )

        #now saving the model in trained path
        Save_Model(filepath=Path(self.config.trained_model_path),model=self.model)