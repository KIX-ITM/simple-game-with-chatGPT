import logging

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from model import models, schemas, crud
from model.database import SessionLocal, engine
from controller import question

models.Base.metadata.create_all(bind=engine)

application = FastAPI()

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @application.get('/test', response_model=schemas.Question)
@application.get('/test')
def test(db: Session = Depends(get_db)):
    words = crud.get_all_words(db)
    genres = crud.get_all_genre_id(db)
    options = question.create_three_option(words, genres)
    return options



