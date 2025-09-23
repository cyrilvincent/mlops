import pickle
from typing import List
import pandas as pd
import numpy as np
import pickle
import sklearn.linear_model as lm


class HouseSklearnService:

    def __init__(self, path):
       self.path = path
       self.dataframe = pd.read_csv(path)
       self.y = self.dataframe["loyer"]
       self.x = self.dataframe["surface"].values.reshape(-1, 1)
       self.model = lm.LinearRegression()

    def train(self):
        self.model.fit(self.x, self.y)

    def predict(self, surface: float):
        matrix = np.array([surface]).reshape(-1, 1)
        res = self.model.predict(matrix)
        return int(res[0])

    def predicts(self, surfaces: List[float]):
        matrix = np.array(surfaces).reshape(-1, 1)
        res = self.model.predict(matrix)
        res = [float(x) for x in res]
        return res


class CancerSklearnService:

    def __init__(self, path):
        with open(path, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, vector: List[float]):
        matrix = np.array([vector])
        res = self.model.predict(matrix)
        return int(res[0])

    def predicts(self, matrix: List[List[float]]):
        matrix = np.array(matrix)
        res = self.model.predict(matrix)
        res = [float(x) for x in res]
        return res


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

if __name__ == '__main__':
    house = HouseSklearnService("data/house/house.csv")
    house.train()
    print(house.predict(100))


