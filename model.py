import os
from tensorflow.keras.models import load_model

def load_meso4_weights():
    # Define the path to the pretrained weights file
    weights_path = os.path.join(os.getcwd(), 'weights', 'Meso4_DF')

    # Load the pretrained weights into a Meso4 model object
    meso = Meso4()
    meso.load_weights(weights_path)

    return meso
