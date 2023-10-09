from sqlalchemy.orm import Session

from model import models


def get_all_word(db: Session):
    return db.query(models.WordGenre).all()


def get_all_genre(db: Session):
    return db.query(models.WordGenre).all()