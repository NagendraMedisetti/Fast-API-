from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/add")
def add_numbers(a: int, b: int):
   return {"result": a + b}
 
@app.post("/users")
def create_user(user: dict):
   return {"status": "created", "user": user}