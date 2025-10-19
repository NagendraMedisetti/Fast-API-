from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional
 
app = FastAPI()
 
class User(BaseModel):
   name: str
   email: EmailStr
   age: Optional[int] = None
 
class UserResponse(BaseModel):
   statusCode: int
   name: str
   email: EmailStr
   age: Optional[int] = None
   message: str
   

@app.post("/user", response_model=UserResponse)
def create_user(user: User):
   return UserResponse(
       statusCode=200,
       name=user.name,
       email=user.email,
       age=user.age,
       message="User created successfully"
      #take home : how to add the extra field in the response model which is not present in the request model
   )