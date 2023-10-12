from datetime import datetime

from pydantic import BaseModel


class QuestionBase(BaseModel):
    option_a_ja: str
    option_b_ja: str
    option_c_ja: str
    option_a_en: str
    option_b_en: str
    option_c_en: str
    option_a_is_common: bool
    option_b_is_common: bool
    option_c_is_common: bool
    easy_common_point_ja: str | None = None
    easy_common_point_en: str | None = None
    normal_common_point_ja: str | None = None
    normal_common_point_en: str | None = None
    hard_common_point_ja: str | None = None
    hard_common_point_en: str | None = None


class QuestionCreate(QuestionBase):
    created_at: datetime = None
    updated_at: datetime = None


# レスポンス用のデータモデル（datetime系含まない）
class Question(QuestionBase):
    id: int


    class Config:
        from_attributes = True