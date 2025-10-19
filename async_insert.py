from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from datetime import datetime, timedelta, timezone

app = FastAPI()

DATABASE_URL ="mysql+asyncmy://root:Admin@127.0.0.1:3306/database_connectivity1"


engine = create_async_engine(DATABASE_URL, echo=False)

IST = timezone(timedelta(hours=5, minutes=30))

def current_ist():
    now = datetime.now(IST)
    return now, now.strftime("%Y-%m-%d %H:%M:%S")

@app.post("/insert100")
async def insert_100_rows():

    now_dt, now_str = current_ist()

    rows = []
    for i in range(1, 101):
        rows.append({
            "name": f"User_{i}",
            "email": f"user{i}@example.com",
            "created_at": now_dt,   # same IST timestamp for each row
        })

    insert_sql = text(
        "INSERT INTO users (username, email, created_at) "
        "VALUES (:name, :email, :created_at)"
    )

    async with engine.begin() as conn:
        await conn.execute(insert_sql, rows)

    return {
        "message": "100 users inserted successfully",
        "timestamp_ist": now_str
    }