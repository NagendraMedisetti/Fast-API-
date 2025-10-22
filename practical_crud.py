from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.post("/post-users")
def post_sam():
    return {"message": "This is a POST request"}

@app.get("/get-users")
def get_sam():
    return {"message": "This is a GET request"}

@app.put("/put-users")
def put_sam():
    return {"message": "This is a PUT request"}

@app.delete("/delete-users")
def delete_sam():
    return {"message": "This is a DELETE request"}

@app.patch("/patch-users")    
def patch_sam():
    return {"message": "This is a PATCH request"}