from typing import Any
import uvicorn
from fastapi import FastAPI, Body
import sklearn_service
import os
from fastapi.middleware.cors import CORSMiddleware

is_prod = "env" in os.environ and os.environ["env"] == "prod"

app = FastAPI(
    docs_url=None if is_prod else "/docs",
    redoc_url=None,
    openapi_url=None if is_prod else "/openapi.json",
)

cors = ["https://my_url.com", "https://www.my_url.com"]
if not is_prod:
    cors += ["http://localhost", "http://127.0.0.1", "https://localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)


house_service = sklearn_service.HouseSklearnService("data/house/house.csv")
mnist_service = sklearn_service.MnistSklearnService("data/mnist/rf-93.pickle")
cancer_service = sklearn_service.CancerSklearnService("data/cancer/rf-94.pickle")


@app.get("/")
def root():
    return "Hello World"


@app.get("/house/{surface}")
def house(surface: int):
    house_service.train()
    return house_service.predict(surface)


@app.post("/cancer")
def cancer(features: Any = Body(...)):
    print(f"Cancer: {features}")
    res = cancer_service.predict(features)
    print(f"Cancer: {res}")
    return res


@app.post("/mnist")
def mnist(features: Any = Body(...)):
    res = mnist_service.predict(features)
    print(f"MNIST: {res}")
    return res


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
