import pickle
from typing import List

import numpy as np
import sklearn.model_selection as ms
import sklearn.ensemble as tree
import sklearn.svm as svm
import pickle

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



