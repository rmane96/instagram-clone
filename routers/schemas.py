from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from db.models import UserModel


class UserBase(BaseModel):
    username: str
    email:str
    password:str
    

class UserDisplay(BaseModel): 
    username : str
    email :str
    class Config(): #need to convert from orm to json or it gives error --> not a valid dict -- type error
        orm_mode = True

class User(BaseModel):
    username:str
    class Config():
        orm_mode = True
        

class UserAuth(BaseModel):
    id:int
    username:str
    
    
    

class PostBase(BaseModel):
    image_url:str
    image_url_type:str
    caption:str
    
    

# for post display

    
class PostDisplay(BaseModel):
    id: int
    image_url_type: str
    caption: str
    creator_id: int
    timestamp: datetime
    creator_username : str 
    
    class Config():
        orm_mode = True
        

        
    


