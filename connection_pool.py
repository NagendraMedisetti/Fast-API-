from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()
DATABASE_URL = "mysql+pymysql://root:Admin@127.0.0.1:3306/database_connectivity1"
engine = create_engine(
    DATABASE_URL,
    pool_size=5,         # Number of persistent connections
    max_overflow=10,     # Extra temporary connections if all are busy
    pool_timeout=30,     # Seconds to wait before giving up
    pool_recycle=1800,   # Recycle connections every 30 mins
    pool_pre_ping=True,  # Check connection before using
    echo=True            # Log SQL in console (for learning)
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT id, username, email FROM users LIMIT 10"))
    users = [dict(row._mapping) for row in result]
    return {"users": users}