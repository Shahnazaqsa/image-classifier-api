import tensorflow as tf
import numpy as np 
import cv2
from PIL import Image

# load cnn model

model = tf.keras.models.load_model('model/mnist_cnn_model.h5')

def image_prediction(image_pil):
    # convert PIL image to numpy array
    image  = np.array(image_pil)
    # invert image if bacground is dark
    if np.mean(image) < 127:
        image = 255 - image
    # apply threshold to clean the image
    _, image = cv2.threshold(image, 128, 255 ,cv2.THRESH_BINARY )
    # resize
    image = cv2.resize(image,(28,28))
    #normalize
    image = image.astype('float32')/255.0
    #reshape to match the model input
    image = image.reshape(1, 28 , 28 , 1)
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)
    
    
    return predicted_class