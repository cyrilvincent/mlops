import pickle
from typing import List

import numpy as np
import sklearn.model_selection as ms
import sklearn.ensemble as tree
import sklearn.svm as svm
import pickle

class MnistSklearnService:

    def __init__(self, path):
        with open(path, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, matrix: List[List[int]]):
        cube = np.array([matrix])
        res = self.model.predict(cube.reshape(1, 28*28))
        return int(res[0])

    def predicts(self, cube: List[List[List[int]]]):
        cube = np.array(cube)
        res = self.model.predict(cube.reshape(-1, 28*28))
        res = [int(x) for x in res]
        return res

class CancerSklearnService:

    def __init__(self, path):
        with open(path, "rb") as f:
            self.scaler, self.model = pickle.load(f)

    def predict(self, vector: List[float]):
        matrix = np.array([vector])
        normalized = self.scaler.transform(matrix)
        res = self.model.predict(normalized)
        return int(res[0])

    def predicts(self, matrix: List[List[float]]):
        matrix = np.array(matrix)
        normalized = self.scaler.transform(matrix)
        res = self.model.predict(normalized)
        res = [float(x) for x in res]
        return res



