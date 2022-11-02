from db.models import UserModel
from routers.schemas import UserBase
from sqlalchemy.orm import Session
from db.hashing import Hash
from fastapi import HTTPException, status


def create_user(db:Session,request:UserBase):
    new_user = UserModel(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_username(db:Session, username: str):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
        raise HTTPException(status=status.HTTP_404_NOT_FOUND, 
                            details=f"User with username: {username} not found")
    return user


