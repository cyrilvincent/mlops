import matplotlib.pyplot as plt
import argparse
import json


with open("data/mnist/mnist_2.json") as f:
    matrix = json.load(f)

plt.axis('off')
plt.imshow(matrix,cmap=plt.cm.gray_r,interpolation="nearest")
plt.show()