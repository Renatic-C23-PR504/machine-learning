import os 
from io import BytesIO
from PIL import Image
from flask import Flask, request, jsonify, make_response
import requests
import tensorflow as tf
import numpy as np


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)
class_names = ['No DR', 'Mild', 'Moderate', 'Severe', 'Proliferative DR']

# eye and no-eye model
eye_classification_model = tf.keras.models.load_model('./eyes_classification/Eyes_Classification_Model.h5')
# diabetic retinopathy model
dr_classification_model = tf.keras.models.load_model('./diabetic_retinopathy_classification/model_mobilenet_dr.h5')

def transform_image(img, img_shape):
    img = img.convert("RGB")
    img = img.resize((img_shape, img_shape))
    input_arr = tf.keras.utils.img_to_array(img)
    input_arr = tf.cast(img, dtype=tf.float32)/255
    input_arr = np.expand_dims(input_arr, axis=0)
    return input_arr
    
def predict_eye_image(input_arr):
    prediction = eye_classification_model.predict(input_arr)
    # 0 mean that there are eye
    # 1 mean that there are no eye
    # it was because folder order
    if np.round_(prediction[0]) == 0:
        return True
    elif np.round_(prediction[0]) == 1:
        return False

def predict_dr_image(input_arr):
    prediction = dr_classification_model.predict(input_arr)
    predicted_class = class_names[np.argmax(prediction)]
    return predicted_class
    
@app.route("/", methods=["GET"])
def index():
    dict = {
        'message': 'API SUCCESS',
        'status': 'success',
        'error': False
    }
    response = make_response(jsonify(dict))
    response.headers['Content-Type'] = 'application/json'
    response.status_code = 200
    return response

@app.route("/predict", methods = ["POST"]) 
def predict():
    if 'image_url' in request.json:
        image_url = request.json['image_url']
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        dr_img = transform_image(img, 224) # old model using 224x224
        # dr_img = transform_image(img, 350) # new model using 350x350
        eye_img = transform_image(img, 150)
        
        # make predictions to detect if the image has retina on it
        eye_prediction = predict_eye_image(eye_img)
        if eye_prediction:
            # make predictions to detect severe levels of 
            # diabetic retinopathy
            dr_prediction = predict_dr_image(dr_img)
            dict = {
                'message': 'Diabetic Retinopathy Level',
                'error': False,
                'retina_detected': eye_prediction,
                'dr_class': dr_prediction
            }
            return jsonify(dict)
        dict = {
            'message': 'Retina tidak terdeteksi',
            'error': False,
            'retina_detected': eye_prediction,
            'dr_class': ''
        }
        return jsonify(dict)
    
if __name__ == "__main__":
    app.run(debug = True)
