import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return True


@app.get("/hello/{p}")
async def hello(p: str):
    return {"message": "Hello " + p}




if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)

