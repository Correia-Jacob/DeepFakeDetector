from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Load pre-trained model
model = tf.keras.models.load_model('model.h5')

# Define class names for classification
class_names = ['Real', 'DeepFake']


# Define function for loading and preprocessing image
def load_image(image_file):
    img = image.load_img(image_file, target_size=(256, 256))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    return img


# Define route for homepage
@app.route('/')
def home():
    return render_template('index.html')


# Define route for handling image upload and classification
@app.route('/upload', methods=['POST'])
def upload():
    # Get uploaded image file
    image_file = request.files['image']

    # Load and preprocess image
    img = load_image(image_file)

    # Make prediction
    prediction = model.predict(img)[0]
    class_index = np.argmax(prediction)
    class_name = class_names[class_index]
    probability = prediction[class_index]

    # Return result as JSON
    result = {'class_name': class_name, 'probability': float(probability)}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
