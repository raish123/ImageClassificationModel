from flask import Flask,render_template,redirect,url_for,request,jsonify
import os
from flask_cors import cross_origin,CORS
from src.ImageClassifier.Utils import decode_image,encode_image
from src.ImageClassifier.Pipelines.predict import DogCat

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

#creating route to show default or rendener index.html
@app.route('/',methods=['GET'])
@cross_origin()
def index():
    return render_template('index.html')



class ClientApp():
    def __init__(self):
        #user given  image changing them into jpg format
        self.filename = "inputImage.jpg"
        #creating an object of dogcat class
        self.classifier = DogCat(filename=self.filename)


#creating route for prediction
@app.route("/predict", methods=['GET','POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decode_image(image,clApp.filename) #clApp object of clientapp class
    result = clApp.classifier.Predict()
    return jsonify(result)


#creating a route for training
@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py") #system method of os module we pass the command to be executed
    return "Training done successfully!"




if __name__ == '__main__':
    #object of clientapp class
    clApp = ClientApp()
    app.run(debug=True,host="0.0.0.0",port=8080)
