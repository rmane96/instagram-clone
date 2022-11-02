from sqlalchemy.orm import Session
from routers.schemas import PostBase
from db.models import PostModel
import datetime


def create(db:Session, request:PostBase,user):
    new_post = PostModel(
    image_url= request.image_url,
    image_url_type= request.image_url_type,
    caption= request.caption,
    timestamp= datetime.datetime.now(),
    creator_username = user.username
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all(db:Session):
    return db.query(PostModel).all()