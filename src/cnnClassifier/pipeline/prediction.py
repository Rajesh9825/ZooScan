import numpy as np
from tensorflow.keras.model import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self,filename):
        self.filename = filename



    def predict(self):
        # load Model
        model = load_model(os.path.join("artifacts","training","model.h5"))

        # Preprocess image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Make prediction
        prediction_proba = model.predict(test_image)
        predicted_class_index = np.argmax(prediction_proba,axis=1)[0]
       

        # Map class index to label
        class_names = ['cat', 'dog', 'snake']  #  Replace with your actual classes
        predicted_class_label = class_names[predicted_class_index]

        return [{"image": predicted_class_label}]

        # if result[0] == 1:
        #     prediction = 'cat'
        #     return [{"image" : prediction}]
        # else: 
        #     prediction = 'dog'
        #     return [{"image": prediction}]