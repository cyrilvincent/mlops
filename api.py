from flask import Flask, jsonify, request
import pickle
import numpy as np
import sklearn_service
app = Flask(__name__)
mnist_service = sklearn_service.MnistSklearnService("data/mnist/rf-93.pickle")
cancer_service = sklearn_service.CancerSklearnService("data/cancer/rf-94.pickle")

@app.route("/")
def root():
    return jsonify("Hello World")

@app.route("/house/<int:surface>")
def house(surface):
    with open("data/house/house.pickle", "rb") as f:
        model = pickle.load(f)
    y_res = model.predict(np.array([[surface]]))
    return jsonify(float(y_res[0]))

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
    app.run()

