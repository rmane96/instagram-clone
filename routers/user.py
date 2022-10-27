from fastapi import APIRouter, Depends
from db.database import get_db
from .schemas import UserBase, UserDisplay
from sqlalchemy.orm.session import Session
from db import db_user


router = APIRouter(
    prefix = "/user",
    tags = ["user"]
)

@router.post("/register",response_model=UserDisplay)
def create_user(request:UserBase,db:Session = Depends(get_db)):
    return db_user.create_user(db,request)
    
    




