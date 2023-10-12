import logging

from fastapi import FastAPI, HTTPException, Depends, Request
from sqlalchemy.orm import Session


from model import models, schemas
from model.database import SessionLocal, engine
from controller import question, openai, deepl

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logging.getLogger('sqlalchemy.pool').setLevel(logging.INFO)

models.Base.metadata.create_all(bind=engine)

application = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_authentication_code(req: Request):
    auth_code = req.headers.get("Authorization-Code")
    if not auth_code or not is_valid_auth_code(auth_code):
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return True


# 認証コードの検証を行うダミー関数（実際には適切な検証ロジックを使用してください）
def is_valid_auth_code(auth_code: str):
    return auth_code == "my_authentication_code"


@application.get("/")
async def home(authenticated: bool = Depends(verify_authentication_code)):
    if authenticated:
        return {"detail": "Authenticated successfully"}


@application.get('/questions', response_model=schemas.Question)
def get_options(db: Session = Depends(get_db)):
    result = question.create_options(db)
    if not result:
        raise HTTPException(status_code=404, detail="Failed to create question")
    return result


@application.get('/questions/{question_id}', response_model=schemas.Question)
def get_one_question(question_id: int, difficulty: str, db: Session = Depends(get_db)):
    question_data = question.get_one_question(db, question_id)
    if not question_data:
        raise HTTPException(status_code=404, detail="Question not found")
    if question.exists_common_point():
        return question_data
    common_point_en = openai.request(question_data, difficulty)
    common_point_ja = deepl.request(common_point_en)
    return question.update_common_point(db, question_id, difficulty, common_point_en, common_point_ja)

