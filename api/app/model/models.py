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
    option_a = Column(String, nullable=False)
    option_b = Column(String, nullable=False)
    option_c = Column(String, nullable=False)
    option_a_is_common = Column(Boolean, nullable=False)
    option_b_is_common = Column(Boolean, nullable=False)
    option_c_is_common = Column(Boolean, nullable=False)
    common_point_japanese = Column(String, nullable=True)
    common_point_english = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)

