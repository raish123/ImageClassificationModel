import tensorflow
from pathlib import Path
from src.ImageClassifier.Config import EvaluatingModelConfig
from src.ImageClassifier.Utils import write_json_file


#In this component file we create a class and initializing the instance variable to entity class variable
#and according to task writing the code

class EvaluatingModel():
    def __init__(self,eval:EvaluatingModelConfig):
        self.eval = eval

    #first loading the trained model
    def trained_model_load(self):
        self.model = tensorflow.keras.models.load_model(
            filepath=Path(self.eval.trained_model_path)
        )

    #2nd method creating ImageDatagenerator for testing data!!
    def _test_image_generator(self):
        #creating keyword argument for test datageenerator
        datagenerator_kwargs = dict(
            rescale=1.0/255,
            validation_split=0.30
        )

        #dataflow directory keyword argument
        dataflow_kwargs = dict(
            target_size = self.eval.input_shape[:-1],
            interpolation = "bilinear",
            batch_size = self.eval.batch_size,
        )

        #creating testdata generator !!
        test_generator = tensorflow.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        #now passing this test_generator to flow from imagae dtaset directory
        self.test_datagenerator = test_generator.flow_from_directory(
            directory = self.eval.training_data_dir,
            shuffle=False,
            **dataflow_kwargs,
            subset="validation"

        )

    #now evaluating the model
    def _evaluating_model(self):
        self.trained_model_load() #rtn model in same class
        self._test_image_generator() #rtn test dataset in same class
        evaluation_results  = self.model.evaluate(self.test_datagenerator)
        return evaluation_results

    #saving the score of model in json!!
    def _saving_score(self):
        result = self._evaluating_model()
        fileapth = "score.json"
        data = {"loss":result[0],"accuracy":result[1]}
        write_json_file(filepath=Path(fileapth),data=data)



