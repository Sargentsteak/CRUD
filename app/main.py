from typing import Optional
from fastapi import FastAPI , Response, status, HTTPException ,Depends
from fastapi.params import Body
from pydantic import BaseModel, errors
# from passlib.context import CryptContext
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user
from . import schemas , models
from .database import engine ,SessionLocal , get_db
from .routers import user, post 
from . import auth

# pwd_context = CryptContext(schemes =["bcrypt"] , deprecated = "auto")
models.Base.metadata.create_all(bind=engine)

app = FastAPI() 

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello man "}


    


    

