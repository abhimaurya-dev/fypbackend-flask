from flask import Flask
from flask import request
from flask_cors import CORS
import numpy as np
import pickle

app = Flask(__name__)

CORS(app)

@app.route("/")
def hello_world():
    return "<div style='overflow:hidden; width:100%; height:100%;'><h1 style='display:flex; align-items:center; justify-content:center; width:100vw; font-size:4rem; height:100vh'>Welcome To Final Year Project</h1></div>"

@app.route("/predict/", methods=['POST'])
def recommendCrop():
    setMessage = "true"
    try:
        query_array = request.json['query_array']
        setMessage="NO MODEL"
        query_array = list(map(float,query_array))
        query_array = np.array(query_array).reshape(1,-1)
        response_data={}
        with open("mlmodel\\trainedModel\\trained_model",'rb') as f:
          model = pickle.load(f)
          predict_result = model.predict(query_array)
          response_data['success'] = 'true'
          response_data['predicted_crop'] = predict_result[0]
        return response_data
    except:
        return {
                  'success': 'false',
                  'message':'Invalid request',
                  'dev': setMessage
              }