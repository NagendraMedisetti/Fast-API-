from fastapi import FastAPI, Depends, HTTPException, Header
app = FastAPI()
def get_current_user(token: str = Header(None)):
   if token != "secret123":
       raise HTTPException(status_code=401, detail="Invalid or missing token")
   return {
       "id": 1,
       "name": "Avinash Seth",
       "email": "avinash@demo.com"
   }


 
@app.get("/me")
def profile(user = Depends(get_current_user)):
   return {"message": f"Welcome, {user['name']}!"}

# inorder to test use /profile?token=secret123