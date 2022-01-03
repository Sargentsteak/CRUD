from typing import Text
from sqlalchemy import column , Integer , String
from sqlalchemy.sql.expression import false, null, text, true
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, Boolean
from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column (Integer, primary_key=true , nullable=False)
    title  = Column(String , nullable= False)
    content = Column(String , nullable = False)
    published = Column(Boolean , server_default= 'True', nullable=False)
    created_at = Column(TIMESTAMP(timezone = True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id" , ondelete="CASCADE") , nullable=False)

class User(Base):
    __tablename__ = "users"
    
    id = Column (Integer, primary_key=true , nullable=False) 
    email= Column(String, nullable=False, unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone = True), nullable=False, server_default=text('now()'))

 