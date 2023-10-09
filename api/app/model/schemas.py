from datetime import datetime

from pydantic import BaseModel


class QuestionBase(BaseModel):
    option_a: str
    option_b: str
    option_c: str
    option_a_is_common: bool
    option_b_is_common: bool
    option_c_is_common: bool
    common_point_japanese: str | None = None
    common_point_english: str | None = None


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True