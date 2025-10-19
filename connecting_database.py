from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:Admin@127.0.0.1:3306/database_connectivity"

engine = create_engine(DATABASE_URL)

@app.get("/")
def home():
    return {"message": "Connected to MySQL successfully!"}

@app.get("/users")
def get_users(limit:int=5):    
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT id, username, email FROM users LIMIT {limit}"))
        rows = result.mappings().all()
    return {"data": rows}