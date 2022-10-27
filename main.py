from fastapi import FastAPI
from db import models
from db.database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.get("/")
def root():
    return {"message":"This is Root"}