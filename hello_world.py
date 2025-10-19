# pip install "fastapi[standard]"

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    mysum = 2+4
    return{"Helloworld": f"Hello, World! Sum is : {mysum}"}

@app.get("/hello/{name}")
def read_name(name: str):
    if name==' ':
        return 'Please provide a name'
    else:
        return {"statement": f"Hi, {name}! How are you today?"}