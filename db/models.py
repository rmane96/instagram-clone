from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('PostModel',back_populates='user')


class PostModel(Base):
    __tablename__ = 'post'
    id = Column(Integer,primary_key=True,index=True)
    image_url= Column(String)
    image_url_type= Column(String)
    caption= Column(String)
    timestamp= Column(DateTime)
    creator_id= Column(Integer, ForeignKey('user.id'))
    user = relationship('UserModel', back_populates='items')
    
    
    