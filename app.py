import os 
import tensorflow as tf
from PIL import Image
import numpy as np
from flask import Flask, request, jsonify, make_response, send_file
import requests
from io import BytesIO


# from google.cloud import storage


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)
class_names = ['No DR', 'Mild', 'Moderate', 'Severe', 'Proliferative DR']


# pertama masukin ke model ini dulu buat klasifikasi mata
eye_classification_model = tf.keras.models.load_model('.\Eyes_classification\Eyes_Classification_Model.h5')
# baru masukin ke model ini buat klasifikasi penyakitnya
dr_classification_model = tf.keras.models.load_model('.\diabetic_retinopathy_classification\model_mobilenet_dr.h5')

def transform_image(img, img_shape):
    input_arr = tf.keras.utils.img_to_array(img)
    input_arr = tf.image.resize(input_arr, [img_shape, img_shape])
    # input_arr = tf.cast(img, dtype=tf.float32)/255
    input_arr = np.expand_dims(input_arr, axis=0)
    return input_arr
    
def predict_eye_image(input_arr):
    prediction = eye_classification_model.predict(input_arr)
    if prediction[0] == 1:
        return True
    elif prediction[0] == 0:
        return False

def predict_dr_image(input_arr):
    prediction = dr_classification_model.predict(input_arr)
    predicted_class = class_names[np.argmax(prediction)]
    return predicted_class
    
    
    """def predict():
    if 'image_url' in request.json:
        image_url = request.json['image_url']
        image = tf.keras.utils.load_img(response.content, target_size=(350,350))
    
    elif 'bucket_name' in request.json and 'image_path' in request.json:
        bucket_name = request.json['bucket_name']
        image_path = request.json['image_path']

        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(image_path)
        image = tf.keras.utils.load_img(blob.download_as_text(), target_size=(350,350))
        
    else:
        return jsonify({'error': 'Invalid request'}), 400
    
    image = transform_image(image)
    prediction = predict_image(eye_classification_model, image)
    predicted_class = np.argmax(prediction)
    
    return jsonify({'class': predicted_class})"""
    
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
        dr_img = transform_image(img, 350)
        eye_img = transform_image(img, 150)
        
        return jsonify({'shape': eye_img.tolist()})
    
        # make predictions to detect if image is a eye/retina
        eye_prediction = predict_eye_image(eye_img)
        if eye_prediction:
            dr_prediction = predict_dr_image(dr_img)
            dict = {
                'message': 'Diabetic Retinopathy Level',
                'error': False,
                'class': dr_prediction
            }
            return jsonify(dict)
        dict = {
            'message': 'Retina tidak terdeteksi',
            'error': False,
            'class': eye_prediction
        }
        return jsonify(dict)
        
        
        if img:
            dict = {
                'message': 'API SUCCESS',
                'error': False
            }
            response = make_response(jsonify(dict))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 200

            return response
    
    
if __name__ == "__main__":
    app.run(debug = True)
