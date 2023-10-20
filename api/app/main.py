import os
import logging

from fastapi import FastAPI, HTTPException, Depends, Request
from sqlalchemy.orm import Session


from app.model import models, schemas
from app.model.database import SessionLocal, engine
from app.controller import question, openai, deepl

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
    # 認証コードの判定
    auth_code = req.headers.get("Authorization-Code")
    if not auth_code or not is_valid_auth_code(auth_code):
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return True


def is_valid_auth_code(auth_code: str):
    # 認証コードの検証を行うダミー関数
    return auth_code == os.getenv("FASTAPI_AUTH_KEY")


@application.get("/")
async def home(authenticated: bool = Depends(verify_authentication_code)):
    # 認証コードテスト用
    if authenticated:
        return {"detail": "Authenticated successfully"}


@application.get('/questions', response_model=schemas.Question)
def get_options(db: Session = Depends(get_db)):
    # 選択肢を3つ用意-QuestionDBにレコード作成-レコード返す
    result = question.create_options(db)
    if not result:
        # 作成失敗した場合はエラー
        raise HTTPException(status_code=400, detail="Failed to create question")
    return result

@application.get('/questions/{question_id}/{difficulty}', response_model=schemas.Question)
def get_one_question(question_id: int,
                     difficulty: str,
                     db: Session = Depends(get_db),
                     authenticated: bool = Depends(verify_authentication_code)
                     ):
    # idからレコード検索-選択肢と難易度から共通点を作成-レコード更新-更新したレコードを返す
    question_data = question.get_one_question(db, question_id)
    if not question_data:
        # 検索結果がない場合はエラー
        raise HTTPException(status_code=404, detail="Question not found")
    if question.exists_common_point(question_data, difficulty):
        # レコード検索結果に指定難易度の共通点が含まれる場合は、検索結果を返す
        return question_data
    common_point_en = openai.request(question_data, difficulty)
    common_point_ja = deepl.request(common_point_en)
    return question.update_common_point(db, question_id, difficulty, common_point_en, common_point_ja)

