from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user,post
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)

models.Base.metadata.create_all(engine)

app.mount('/images',StaticFiles(directory='images'),name='images')

@app.get("/")
def root():
    return {"message":"This is Root"}