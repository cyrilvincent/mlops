import uvicorn
from fastapi import FastAPI
import sklearn_service
import config

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Sklearn API"}


@app.get("/health")
async def health():
    return True


@app.get("/version")
async def version():
    return config.version


@app.get("/house/{surface}")
async def house(surface: int):
    house_service = sklearn_service.HouseSklearnService(config.house_path)
    house_service.train()
    loyer = house_service.predict(surface)
    return loyer


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)