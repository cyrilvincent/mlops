from typing import List

import tensorflow as tf
class DogsVsCatsService:

    def __init__(self, path):
        self.model = tf.keras.models.load_model(path)

    def predict(self, path: str):
        img = tf.keras.preprocessing.image.load_img(path, target_size=(224, 224))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img *= 1. / 255
        img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
        res = self.model.predict(img)[0][0] # image 0, output 0
        s = "dog"
        if res < 0.5:
            s = "cat"
            res = 1 - res
        return s, float(res)




