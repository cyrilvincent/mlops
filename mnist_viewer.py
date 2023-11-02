import matplotlib.pyplot as plt
import argparse
import json


parser = argparse.ArgumentParser(description="MNIST Viewer")
parser.add_argument("path", help="Path of json")
args = parser.parse_args()

with open(args.path) as f:
    matrix = json.load(f)

plt.axis('off')
plt.imshow(matrix,cmap=plt.cm.gray_r,interpolation="nearest")
plt.show()