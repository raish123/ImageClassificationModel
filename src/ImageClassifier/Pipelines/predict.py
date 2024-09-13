#in this Module user give image to us ... we have to do preprocessing and give show them prediction resul
import tensorflow
from tensorflow.keras.models import load_model
import numpy
from tensorflow.keras.preprocessing import image
import os,sys
from src.ImageClassifier.Exception import CustomException
from src.ImageClassifier.loggers import logger


class DogCat():
    #user giving us image file we take as instance variable
    def __init__(self,filename):
        self.filename = filename


    #creating method to predict image
    def Predict(self):
        #load the customized after training
        model = load_model(os.path.join("artifacts","training","model.h5"))

        imagefilename = self.filename

        #resizing,converting to array,changing dimension the image file 
        # to 224*224 width and height of pixel
        test_img = image.load_img(imagefilename, target_size=(224, 224))
        test_img = image.img_to_array(test_img) #converting to numpy array
        test_img = numpy.expand_dims(test_img,axis=0)

        result = numpy.argmax(model.predict(test_img),axis=1)
        logger.info(f"the result of test image is : {result}")
        print(result)

        if result[0] == 1:
            prediction = "Dog"
            return [{'image': prediction}]  
        else:
            prediction = "Cat"
            return [{'image': prediction}]

