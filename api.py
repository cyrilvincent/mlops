import numpy as np
from flask import Flask, request, jsonify
import pickle
import cancer_sklearn_service
import sklearn_service


app = Flask(__name__)
cancer_service = sklearn_service.CancerSklearnService("data/cancer/rf-97.pickle")
mnist_service = sklearn_service.MnistSklearnService("data/mnist/rf-93.pickle")

@app.route("/")
def root():
    return jsonify("hello")

@app.route("/house/<int:surface>")
def house(surface):
    matrix = np.array([[surface]])
    with open("data/house/house.pickle", "rb") as f:
        model = pickle.load(f)  # Slow
    res = model.predict(matrix) #Bad, need a service
    return jsonify(float(res[0]))

@app.route("/cancer", methods=['POST'])
def cancer():
    features = request.json
    print(f"Cancer: {features}")
    res = cancer_service.predict(features)
    print(f"Cancer: {res}")
    return jsonify(res)

@app.route("/mnist", methods=['POST'])
def mnist():
    features = request.json
    res = mnist_service.predict(features)
    print(f"MNIST: {res}")
    return jsonify(res)


if __name__ == '__main__':
    app.run(host="0.0.0.0")

