import json
import pickle
import numpy as np
import sklearn.model_selection as ms
import sklearn.ensemble as tree
import sklearn.svm as svm
import pickle

class NumpyArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

with np.load("mnist.npz", allow_pickle=True) as f:
    x_train, y_train = f["x_train"], f["y_train"] # 60000
    x_test, y_test = f["x_test"], f["y_test"] # 10000

for i in range(10):
    for x, y in zip(x_test, y_test):
        if i == y:
            with open(f"mnist_{i}.json", "w") as f:
                json.dump(x, f, cls=NumpyArrayEncoder)
            break
