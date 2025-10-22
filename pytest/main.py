from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
   return {"message": "Hello, FastAPI!"}
 
@app.get("/greet/{name}")
def greet(name: str):
   return {"message": f"Hello, {name}!"}

@app.get("/vote/{age}")
def can_vote(age: int):
   if age >= 18:
       return {"message": "You are eligible to vote."}
   else:
       return {"message": "You are not eligible to vote yet."}

# inorder to run this use pytest -v

