import uuid
from typing import Any

import tensorflow as tf
import uvicorn
from fastapi import FastAPI, Body, File, UploadFile

import tensorflow_service

app = FastAPI()

image_service = tensorflow_service.ImageNet()
cancer_service = tensorflow_service.CancerTFService("data/cancer/mlp.h5", "data/cancer/mlp_scaler.pickle")
mnist_service = tensorflow_service.MNISTTFService("data/mnist/cnn.h5")


@app.get("/")
def root():
    return tf.__version__


@app.post("/cancer")
def cancer(features: Any = Body(...)):
    print(f"Cancer: {features}")
    res = cancer_service.predict(features)
    print(f"Cancer: {res}")
    return res


@app.post("/imagenet")
def imagenet(image: UploadFile = File(...)):
    data = image.file.read()
    file = f"temp/imagenet_{uuid.uuid4()}.png"
    print(f"Write {file}")
    with open(file, "wb") as f:
        f.write(data)
    res = image_service.predict(file)
    print(f"ImageNet: {res}")
    return res


@app.post("/mnist")
def mnist(features: Any = Body(...)):
    res = mnist_service.predict(features)
    print(f"MNIST: {res}")
    return res


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
