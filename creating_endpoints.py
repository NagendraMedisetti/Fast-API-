from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "this is home page"}

@app.get("/nagendra")
def nagendra():
    return {"message": "this is nagendra page"}
