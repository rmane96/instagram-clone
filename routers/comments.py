from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import CommentModel
from routers.schemas import CommentBase
from auth.oauth2 import get_current_user
from routers.schemas import UserAuth
from db import db_comments


router = APIRouter(
    prefix='/comment',
    tags=['comments']
)

@router.get('/all/{post_id}')
def comments(post_id:int,db:Session=Depends(get_db)):
    return db_comments.get_all(db,post_id)

@router.post('')
def create(request:CommentBase,db:Session = Depends(get_db),current_user:UserAuth=Depends(get_current_user)):
    return db_comments.create(db,request)
    

    