import uuid
from typing import Any
import tensorflow as tf
import uvicorn
import config
from fastapi import FastAPI, Body, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os

import tensorflow_service

is_prod = "env" in os.environ and os.environ["env"] == "prod"

app = FastAPI(
    docs_url=None if is_prod else "/docs",
    redoc_url=None,
    openapi_url=None if is_prod else "/openapi.json",
)

cors = ["http://www.cyrilvincent.com", "https://www.cyrilvincent.com"]
if not is_prod:
    cors += ["http://localhost", "http://127.0.0.1"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)

image_service = tensorflow_service.ImageNet()
cancer_service = tensorflow_service.CancerTFService(config.cancer_tf_path, config.cancer_scaler_path)
mnist_service = tensorflow_service.MNISTTFService(config.mnist_tf_path)


@app.get("/")
def root():
    return tf.__version__


@app.get("/version")
def version():
    return {'version': config.version}


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

