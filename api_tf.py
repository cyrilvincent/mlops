import json
import uuid
import tensorflow as tf
from flask import Flask, request, jsonify
import tensorflow_service
import numpy_serializer

app = Flask(__name__)
image_service = tensorflow_service.ImageNet()
pet_service = tensorflow_service.DogsVsCatsService("data/dogsvscats/cnn-77.h5")
cancer_service = tensorflow_service.CancerTFService("data/cancer/mlp.h5", "data/cancer/mlp_scaler.pickle")
mnist_service = tensorflow_service.MNISTTFService("data/mnist/cnn.h5")
driver_service = tensorflow_service.DriverService("data/drivers/model.h5")
denoise_service = tensorflow_service.MnistNoiseService("data/mnist/ae_encoder.h5", "data/mnist/ae_decoder.h5")


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

@app.route("/pets", methods=['POST'])
def pets():
    data = request.files['image'].stream.read()
    file = f"temp/pets_{str(uuid.uuid4())}.png"
    print(f"Write {file}")
    with open(file, "wb") as f:
        f.write(data)
    res = pet_service.predict(file)
    print(f"Pets: {res}")
    return jsonify(res)

@app.route("/drivers", methods=['POST'])
def drivers():
    data = request.files['image'].stream.read()
    file = f"temp/drivers_{str(uuid.uuid4())}.png"
    print(f"Write {file}")
    with open(file, "wb") as f:
        f.write(data)
    res = driver_service.predict(file)
    print(f"Drivers: {res}")
    s = json.dumps(res, cls=numpy_serializer.NumpyArrayEncoder)
    return jsonify(eval(s))

@app.route("/denoise", methods=['POST'])
def denoise():
    features = request.json
    res = denoise_service.predict(features)
    print(f"MNIST Denoise: {res}")
    s = json.dumps(res, cls=numpy_serializer.NumpyArrayEncoder)
    return jsonify(eval(s))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)

