from random import random
from fastapi import APIRouter, Depends, status, File
from db.database import get_db
from sqlalchemy.orm import Session
from routers.schemas import PostBase, PostDisplay  
from fastapi.exceptions import HTTPException
from db import db_post
from typing import List
from fastapi.datastructures import UploadFile
import random, string, shutil


router = APIRouter(
    prefix = "/post",
    tags = ["post"]
)

image_url_types = ['absolute','relative']

@router.post('')
def create(request:PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                            detail="Values can only be absolute or relative")
    return db_post.create(db,request)

@router.get('/all', response_model=List[PostDisplay])
def get_all_post(db:Session = Depends(get_db)):
    return db_post.get_all(db)

@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(10))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.',1))
    path=f'images/{filename}'
    
    with open(path,"w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)
        return {"filename":path} 
    
    
    