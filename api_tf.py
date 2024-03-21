import json
import uuid
import tensorflow as tf
from flask import Flask, request, jsonify
import tensorflow_service

app = Flask(__name__)
image_service = tensorflow_service.ImageNet()
cancer_service = tensorflow_service.CancerTFService("data/cancer/mlp.h5", "data/cancer/mlp_scaler.pickle")
mnist_service = tensorflow_service.MNISTTFService("data/mnist/cnn.h5")


@app.route("/")
def root():
    return jsonify(tf.__version__)

@app.route("/cancer", methods=['POST'])
def cancer():
    features = request.json
    print(f"Cancer: {features}")
    res = cancer_service.predict(features)
    print(f"Cancer: {res}")
    return jsonify(res)

@app.route("/imagenet", methods=['POST'])
def imagenet():
    data = request.files['image'].stream.read()
    file = f"temp/imagenet_{str(uuid.uuid4())}.png"
    print(f"Write {file}")
    with open(file, "wb") as f:
        f.write(data)
    res = image_service.predict(file)
    print(f"ImageNet: {res}")
    return jsonify(res)

@app.route("/mnist", methods=['POST'])
def mnist():
    features = request.json
    res = mnist_service.predict(features)
    print(f"MNIST: {res}")
    return jsonify(res)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)

