import pickle
from json import JSONEncoder
from typing import Any
import numpy as np
import keras
import abc


class AbstractService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def predict(self, x: Any): ...


class CancerTFService(AbstractService):

    def __init__(self, tf_path, pickle_path):
        self.model = keras.models.load_model(tf_path)
        with open(pickle_path, "rb") as f:
            self.scaler = pickle.load(f)

    def predict(self, features: list[float]) -> tuple[int, float]:
        features = np.array([features])
        normalized = self.scaler.transform(features)
        res = self.model.predict(normalized)[0][0]
        if res > 0.5:
            return 1, float(res)
        return 0, float(1 - res)

    def predicts(self, features: list[list[float]]) -> list[float]:
        features = np.array(features)
        normalized = self.scaler.transform(features)
        res = self.model.predict(normalized, batch_size=len(features), use_multiprocessing=False, workers=1)[0]
        return [float(x) for x in res]


class ImageNet(AbstractService):

    def __init__(self):
        self.model = keras.applications.MobileNetV2()

    def predict(self, path: str) -> tuple[str, float]:
        image = keras.utils.load_img(path, target_size=(224, 224))
        image = keras.utils.img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        image = keras.applications.mobilenet_v2.preprocess_input(image)
        yhat = self.model.predict(image)
        label = keras.applications.mobilenet_v2.decode_predictions(yhat)
        label = label[0][0]
        return label[1], float(label[2])


class MNISTTFService(AbstractService):

    def __init__(self, path):
        self.model = keras.models.load_model(path)

    def predict(self, matrix: list[list[int]]) -> int:
        cube = np.array([matrix], dtype=np.float64)
        cube *= 1/255
        res = self.model.predict(cube)[0]
        return int(res.argmax())

    def predict_top10(self, matrix: list[list[int]]) -> list[float]:
        cube = np.array([matrix], dtype=np.float64)
        cube /= 255
        res = self.model.predict(cube)[0]
        return [float(x) for x in res]


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

