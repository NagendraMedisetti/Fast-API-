from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Learning about API versioning"}

# URI Path Versioning (aka URL versioning)

@app.get("/v1/get-name/{name}")
def read_name(name: str):
    return {"statement": f"Hi, {name}! How are you today?"}

@app.get("/v2/get-name/{name}")
def read_name(name: str):
    return {"statement": f"Hi, {name}! How are you today?", "version": "v2"}

# Query Parameter Versioning

@app.get("/get-user-name/{name}")
def get_user_name(name: str, v: int = 1):
    if v == 1:
        return {"statement": f"Hi, my name is {name}", "version": "1"}
    elif v == 2:
        return {"statement": f"My name is {name}", "version": "2"}
    else:
        return {"statement": f"Invalid version code {v}"}