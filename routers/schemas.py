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
    

    


