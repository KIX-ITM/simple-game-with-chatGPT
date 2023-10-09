from sqlalchemy.orm import Session

from model import models, schemas


def get_all_words(db: Session):
    return db.query(models.Word).all()


def get_all_genre_id(db: Session):
    return db.query(models.WordGenre.id).all()


def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()


def create_question(db: Session, question: schemas.QuestionCreate):
    new_question = models.Question(**question.dict())
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question
