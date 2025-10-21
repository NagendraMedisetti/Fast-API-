from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from typing import Optional, List

app = FastAPI(title="Simple User API")

DATABASE_URL = "mysql+pymysql://root:Admin@127.0.0.1:3306/database_connectivity1"
engine = create_engine(DATABASE_URL)

class User(BaseModel):
    username: str
    email: str
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/users")
def create_user(user: User):
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO users (username, email, password) VALUES (:u, :e, :p)"),
            {"u": user.username, "e": user.email, "p": user.password}
        )
        user_id = conn.execute(text("SELECT LAST_INSERT_ID() as id")).scalar()

        user_data = conn.execute(
            text("SELECT id, username, email FROM users WHERE id = :id"),
            {"id": user_id}
        ).mappings().first()
    return user_data

@app.get("/users")
def get_users(limit: int = 10):
    with engine.connect() as conn:
        users = conn.execute(
            text("SELECT id, username, email FROM users LIMIT :limit"),
            {"limit": limit}
        ).mappings().all()
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    with engine.connect() as conn:
        user = conn.execute(
            text("SELECT id, username, email FROM users WHERE id = :id"),
            {"id": user_id}
        ).mappings().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    updates = {}
    if user.username:
        updates["username"] = user.username
    if user.email:
        updates["email"] = user.email
    if user.password:
        updates["password"] = user.password

    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")

    with engine.connect() as conn:
        existing = conn.execute(
            text("SELECT id FROM users WHERE id = :id"),
            {"id": user_id}
        ).first()
        if not existing:
            raise HTTPException(status_code=404, detail="User not found")

        update_fields = ", ".join(f"{field} = :{field}" for field in updates)
        updates["id"] = user_id
        conn.execute(text(f"UPDATE users SET {update_fields} WHERE id = :id"), updates)

        updated = conn.execute(
            text("SELECT id, username, email FROM users WHERE id = :id"),
            {"id": user_id}
        ).mappings().first()
    return updated

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            text("DELETE FROM users WHERE id = :id"),
            {"id": user_id}
        )
    return {"message": "User deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)