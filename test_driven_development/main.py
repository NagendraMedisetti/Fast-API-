from fastapi import FastAPI
app = FastAPI()

@app.get("/vote/{age}")
def can_vote(age: int):
   if age >= 18:
       return {"message": "You can vote"}
   else:
       return {"message": "You cannot vote"}