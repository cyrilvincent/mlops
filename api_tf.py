import uuid
import tensorflow as tf
from flask import Flask, request, jsonify

import dogsvscats_service
import imagenet_service

app = Flask(__name__)
image_service = imagenet_service.ImageNet()
pet_service = dogsvscats_service.DogsVsCatsService("data/dogsvscats/cnn-77.h5")

@app.route("/")
def root():
    return jsonify(tf.__version__)

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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)

