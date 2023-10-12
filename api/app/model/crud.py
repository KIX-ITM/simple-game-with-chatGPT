from sqlalchemy.orm import Session

from model import models, schemas


def get_all_words(db: Session):
    return db.query(models.Word).all()


def get_all_genre_id(db: Session):
    return db.query(models.WordGenre.id).all()


def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()


def create_question(db: Session, question: schemas.QuestionCreate):
    new_question = models.Question(**question)
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question


def update_common_point(db: Session, question_id: int, difficulty: str, en: str, ja: str):
    data = db.query(models.Question).filter(models.Question.id == question_id).first()
    if difficulty == 'easy':
        data.easy_common_point_ja = ja
        data.easy_common_point_en = en
    if difficulty == 'normal':
        data.normal_common_point_ja = ja
        data.normal_common_point_en = en
    if difficulty == 'hard':
        data.hard_common_point_ja = ja
        data.hard_common_point_en = en
    db.commit()
