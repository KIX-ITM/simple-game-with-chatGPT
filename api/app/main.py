import logging

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from model import models
from model.database import SessionLocal, engine
from model import crud

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


@application.get('/test')
def test(db: Session = Depends(get_db)):
    result = crud.get_all_genre(db)
    print(result)
    return result



