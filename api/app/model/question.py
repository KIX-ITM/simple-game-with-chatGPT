from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey

from .settings import engine, Base

class Question(Base):
    """
    QuestionModel
    """
    __tablename__ = 'questions'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    created_at = Column('created_at', DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        'updated_at', DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )
    # 選択肢
    option_a = Column('option_a', String(255), nullable=False)
    option_b = Column('option_b', String(255), nullable=False)
    option_c = Column('option_c', String(255), nullable=False)
    # 選択肢の正解不正解ステータス
    option_a_is_common = Column('option_a_is_common', Boolean, nullable=False)
    option_b_is_common = Column('option_b_is_common', Boolean, nullable=False)
    option_c_is_common = Column('option_c_is_common', Boolean, nullable=False)
    # 共通点_難易度
    common_point_easy_english = Column('common_point_easy_english', String(255), nullable=True)
    common_point_easy_japanese = Column('common_point_easy_japanese', String(255), nullable=True)
    common_point_normal_english = Column('common_point_normal_english', String(255), nullable=True)
    common_point_normal_japanese = Column('common_point_normal_japanese', String(255), nullable=True)
    common_point_hard_english = Column('common_point_hard_english', String(255), nullable=True)
    common_point_hard_japanese = Column('common_point_hard_japanese', String(255), nullable=True)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
