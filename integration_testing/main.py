from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "mysql+pymysql://root:Admin@127.0.0.1:3306/database_connectivity1"

engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)

Base.metadata.create_all(bind=engine)

class UserCreate(BaseModel):
    username: str
    email: EmailStr

app = FastAPI()

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
        db.commit()
    finally:
        db.close()

@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(username=user.username, email=user.email)
    db.add(new_user)
    db.flush()
    return {"id": new_user.id, "username": new_user.username, "email": new_user.email}