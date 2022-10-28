from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email:str
    password:str
    

class UserDisplay(BaseModel): 
    username : str
    email :str
    class Config(): #need to convert from orm to json or it gives error --> not a valid dict -- type error
        orm_mode = True
    

class PostBase(BaseModel):
    image_url:str
    image_url_type:str
    caption:str
    creator_id:int 

# for post display
class User(BaseModel):
    username:str
    class Config():
        orm_mode = True
    
class PostDisplay(BaseModel):
    id: int
    image_url_type: str
    caption: str
    creator_id: int
    timestamp: datetime
    username : str
    
    class Config():
        orm_mode = True
    
    


