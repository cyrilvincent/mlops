import json
from typing import List

import numpy as np
import tensorflow as tf

class TFLiteService:

    def __init__(self, path):
        self.interpreter = tf.lite.Interpreter(model_path=path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        self.input_shape = self.input_details[0]['shape']

    def convert(self, path):
        print(f"Convert {path}")
        model = tf.keras.models.load_model(path)
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        tflite_model = converter.convert()
        with open(path.replace("h5", "tflite"), "wb") as f:
            f.write(tflite_model)

    def predict(self, matrix: List[List[int]]):
        print("Predict")
        x = np.array(matrix, dtype=np.float32)
        x = x.reshape(1,28,28,1)
        x /= 255
        self.interpreter.set_tensor(self.input_details[0]['index'], x)
        self.interpreter.invoke()
        y = self.interpreter.get_tensor(self.output_details[0]['index'])
        return y[0]

if __name__ == '__main__':
    s = TFLiteService("data/mnist/cnn.tflite")
    # s.convert("data/mnist/cnn.h5")
    with open("data/mnist/mnist_0.json") as f:
        x = json.load(f)
    y = s.predict(x)
    print(y)