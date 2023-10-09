from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    japanese = Column(String, nullable=False)
    english = Column(String, nullable=False)
    genre_id = Column(Integer, ForeignKey("word_genres.id"), nullable=False)

    genre = relationship("WordGenre", back_populates="words")


class WordGenre(Base):
    __tablename__ = "word_genres"

    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    genre = Column(String, index=True, nullable=False)

    words = relationship("Word", back_populates="genre")
