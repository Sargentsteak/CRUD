from pydantic import BaseModel, EmailStr
from datetime import datetime



class Postbase(BaseModel):
    title : str
    content :str
    published : bool = True


class PostCreate(Postbase):
    pass


class Post(Postbase):
    id: int 
    created_at : datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email:EmailStr
    password :str

class UserOut(BaseModel):
    id : int
    email : EmailStr

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password :str
