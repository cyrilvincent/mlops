import numpy as np
import sklearn.neighbors as nn
import matplotlib.pyplot as plt
import sklearn.ensemble as rf
from sklearn.tree import export_graphviz
import sklearn.neural_network as nn
import pickle

np.random.seed(42)

num_image=3

with np.load("data/mnist/mnist.npz", allow_pickle=True) as f:
    xtrain, ytrain = f["x_train"], f["y_train"]  # 60000
    xtest, ytest = f["x_test"], f["y_test"]  # 10000

with open(f"data/mnist/mnist-rf-0.97.pickle", "rb") as f:
    model = pickle.load(f)
    x = np.array(xtest[num_image].reshape(-1,28*28))
    ypredicted = model.predict(x)
    print(f"Predicted: {ypredicted}, test: {ytest[num_image]}")

plt.axis('off')
plt.imshow(x[0].reshape(28, 28), cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()