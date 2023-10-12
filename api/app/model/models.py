from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from .database import Base


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, autoincrement=True)
    japanese = Column(String, nullable=False)
    english = Column(String, nullable=False)
    genre_id = Column(Integer, ForeignKey("word_genres.id"), nullable=False)

    genre = relationship("WordGenre", back_populates="words")


class WordGenre(Base):
    __tablename__ = "word_genres"

    id = Column(Integer, primary_key=True, autoincrement=False)
    genre = Column(String, nullable=False)

    words = relationship("Word", back_populates="genre")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    option_a_ja = Column(String, nullable=False)
    option_b_ja = Column(String, nullable=False)
    option_c_ja = Column(String, nullable=False)
    option_a_en = Column(String, nullable=False)
    option_b_en = Column(String, nullable=False)
    option_c_en = Column(String, nullable=False)
    option_a_is_common = Column(Boolean, nullable=False)
    option_b_is_common = Column(Boolean, nullable=False)
    option_c_is_common = Column(Boolean, nullable=False)
    easy_common_point_ja = Column(String, nullable=True)
    easy_common_point_en = Column(String, nullable=True)
    normal_common_point_ja = Column(String, nullable=True)
    normal_common_point_en = Column(String, nullable=True)
    hard_common_point_ja = Column(String, nullable=True)
    hard_common_point_en = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)

