from sqlalchemy.orm import Session

from model import models


def get_all_words(db: Session):
    return db.query(models.Word).all()


def get_all_genre_id(db: Session):
    return db.query(models.WordGenre.id).all()