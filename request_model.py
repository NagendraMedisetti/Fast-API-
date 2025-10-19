from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional
 
app = FastAPI()
 
class User(BaseModel):
   name: str
   email: EmailStr
   age: Optional[int] = None
 
@app.post("/user")
def create_user(user: User):
   return user