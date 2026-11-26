import numpy as np
import matplotlib.pyplot as plt
import sklearn.ensemble as rf
from sklearn.tree import export_graphviz

with np.load("data/mnist/mnist.npz", allow_pickle=True) as f:
    xtrain, ytrain = f["x_train"], f["y_train"]  # 60000
    xtest, ytest = f["x_test"], f["y_test"]  # 10000

print(xtrain.shape, xtest.shape)

xtrain = xtrain.reshape(-1, 28*28) # 784
xtest = xtest.reshape(-1, 28*28)

# Faire un modèle RF
# Apprendre
# Scorer
# Prediction sur le jeux de test

xtest = xtest.reshape(-1, 28, 28)
select = np.random.randint(xtest.shape[0], size=12)

for index, value in enumerate(select):
    plt.subplot(3, 4, index + 1)
    plt.axis("off")
    plt.imshow(xtest[value], cmap=plt.cm.gray_r, interpolation="nearest")
    # plt.title(f"Predicted {ypredicted[value]}")
plt.show()

