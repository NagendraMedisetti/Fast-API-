# from fastapi import FastAPI
# from pydantic import BaseModel, Field
 
# app = FastAPI()
 
# # Define request body schema
# class Username(BaseModel):
#    name: str = Field(..., min_length=3, max_length=20)
 
# @app.post("/check-username")
# def check_username(username: Username):
#    return {"message": "User validated successfully!", "details": username}



from fastapi import FastAPI
from pydantic import BaseModel, validator
 
app = FastAPI()
 
class Username(BaseModel):
   name: str
 
   @validator("name")
   def validate_name(cls, value):
      if len (value) < 3:
            raise ValueError("Username cannot be less than 3 chars")
      elif len(value) > 20:
            raise ValueError("Username cannot be more than 20 chars")
      return value
 
 
@app.post("/check-username")
def check_username(username: Username):
   return {"message": "User validated successfully!", "details": username}