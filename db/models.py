from .database import Base
from sqlalchemy import Column, Integer, String

class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String, unique = True)
    email = Column(String)
    password = Column(String)
    
    