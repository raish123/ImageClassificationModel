from src.ImageClassifier.Exception import CustomException
from src.ImageClassifier.loggers import logger
from src.ImageClassifier.Entity import PrepareBaseModelConfig
import os,sys,tensorflow
from pathlib import Path
from src.ImageClassifier.Utils import Save_Model,read_yaml_file,Create_Directory




#In this component files we gonna initialize the value to 
#preparebasemodel config class variable that having parameter as well as value init
#as well creating method to complete this task of preparebasemodel

class BaseModel():
    #creating construtor to initialize the variable to preparebasemodel class!!
    def __init__(self,config:PrepareBaseModelConfig):
        self.config = config


    #creating method for baseModel 
    def basemodel(self):
        #creating an object for base model
        self.basemodel = tensorflow.keras.applications.vgg16.VGG16(
            weights=self.config.weights,
            include_top=self.config.include_top,
            input_shape=self.config.input_shape,
            classes = self.config.classes
    
        )

        #now saving the base model to artifacts folder
        Save_Model(filepath=Path(self.config.base_model_path),model=self.basemodel) #this model rtn the vgg16 16 layers weights that include cnn layer+ relu layer+pooling+flatten+dense layer now using this model we r creating customize sequentual model

    @staticmethod
    def _prepare_full_custom_model(base_model,freeze,freeze_till,learning_rate,classes):
        #creating a sequential model class object
        sequential_model = tensorflow.keras.models.Sequential()

        #now adding all the vgg16 layers to this sequential model
        for layer in base_model.layers:
            sequential_model.add(layer)

        #now freezing all the cnn layer to sequential model except the dense layers
        if freeze:
            for layer in sequential_model.layers:
                layer.trainable = False #this line show freeze the weights and bias value during training

        elif (freeze_till is not None) and (freeze_till>0):
            for layer in sequential_model.layers[:freeze_till]:
                layer.trainable = False

        #now adding flattern layer to sequential model
        sequential_model.add(tensorflow.keras.layers.Flatten())

        #adding the dense layer to sequential model
        sequential_model.add(tensorflow.keras.layers.Dense(units = classes,activation="sigmoid"))

        

        #now compiling the model
        sequential_model.compile(
            optimizer=tensorflow.keras.optimizers.Adam(learning_rate=learning_rate),
            loss = "binary_crossentropy",
            metrics=["accuracy"]
        )

        #to see the summary of model
        logger.info(sequential_model.summary())

        return sequential_model

        
    def update_base_model(self):
        #creating an object for sequential model
        self.sequential_model = self._prepare_full_custom_model(
            base_model = self.basemodel,
            freeze=True,
            freeze_till=None,
            learning_rate = self.config.learning_rate,
            classes = self.config.classes
        )


        #saving the sequential model to artifacts
        Save_Model(filepath=Path(self.config.update_base_model_path),model=self.sequential_model)
