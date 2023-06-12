import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow import keras
import numpy as np

from flask import Flask, request, jsonify
app = Flask(__name__)

# pertama masukin ke model ini dulu buat klasifikasi mata
eye_classification_model = keras.models.load_model('.\Eyes_classification\Eyes_Classification_Model.h5')
# baru masukin ke model ini buat klasifikasi penyakitnya
dr_classification_model = keras.models.load_model('.\diabetic_retinopathy_classification\model_mobilenet_dr.h5')

def transform_image (image_path):
    img = tf.keras.utils.load_img(image_path, target_size=(350,350))
    input_arr = tf.keras.utils.img_to_array(img)
    input_arr = input_arr / 255.0
    input_arr = tf.image.adjust_contrast(input_arr, 0.7)
    input_arr = tf.image.adjust_brightness(input_arr, 0.3)
    input_arr = tf.image.rgb_to_grayscale(input_arr)
    input_arr = np.array([img])  # Convert single image to a batch.
    # predictions = model.predict(input_arr)
    return input_arr
    
    
@app.route("/predict", methods = ["POST"])
def predict():
    if request.method == 'POST':
        pass
        
    
    
    
if __name__ == "__app__":
    app.run(debug = True)
