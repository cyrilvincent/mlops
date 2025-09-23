from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# CLI : pip install "fastapi[standard]"
# CLI : fastapi dev fastapi_demo.py
