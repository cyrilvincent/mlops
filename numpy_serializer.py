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

if __name__ == '__main__':
    with np.load("data/mnist/mnist.npz", allow_pickle=True) as f:
        x_train, y_train = f["x_train"], f["y_train"] # 60000
        x_test, y_test = f["x_test"], f["y_test"] # 10000

    np.set_printoptions(edgeitems=30, linewidth=100000)
    print(x_test[0])

