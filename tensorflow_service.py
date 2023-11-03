import pickle
from typing import List
import numpy as np
import tensorflow as tf
import numpy_serializer


class CancerTFService:

    def __init__(self, tf_path, pickle_path):
        self.model = tf.keras.models.load_model(tf_path)
        with open(pickle_path, "rb") as f:
            self.scaler = pickle.load(f)

    def predict(self, features: List[float]):
        features = np.array([features])
        normalized = self.scaler.transform(features)
        res = self.model.predict(normalized)[0][0]
        if res > 0.5:
            return 1, float(res)
        return 0, float(1 - res)

class ImageNet:

    def __init__(self):
        self.model = tf.keras.applications.MobileNetV2()

    def predict(self, path):
        image = tf.keras.utils.load_img(path, target_size=(224, 224))
        image = tf.keras.utils.img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
        yhat = self.model.predict(image)
        label = tf.keras.applications.mobilenet_v2.decode_predictions(yhat)
        label = label[0][0]
        return label[1], float(label[2])

class MNISTTFService:

    def __init__(self, path):
        self.model = tf.keras.models.load_model(path)

    def predict(self, matrix: List[List[int]]):
        cube = np.array([matrix], dtype=np.float64)
        cube *= 1/255
        res = self.model.predict(cube)[0]
        return int(res.argmax())

    def predict_top10(self, matrix: List[List[int]]):
        cube = np.array([matrix], dtype=np.float64)
        cube *= 1/255
        res = self.model.predict(cube)[0]
        return [float(x) for x in res]



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

class DriverService:

    def __init__(self, path):
        self.model = tf.keras.models.load_model(path)

    def predict(self, path: str):
        img = tf.keras.preprocessing.image.load_img(path, target_size=(224, 224))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img *= 1. / 255
        img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
        res = self.model.predict(img)[0]
        return res






