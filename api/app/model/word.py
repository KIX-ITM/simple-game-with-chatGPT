from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from .settings import engine, Base


class Word(Base):
    """
    WordModel
    """
    __tablename__ = 'words'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    japanese = Column('japanese', String(255), nullable=False)
    english = Column('english', String(255), nullable=False)
    genre_id = Column(Integer, ForeignKey('word_genres.id'), nullable=False)


class WordGenre(Base):
    """
    WordGenreModel
    """
    __tablename__ = 'word_genres'
    id = Column('id', Integer, primary_key=True, autoincrement=False)
    genre = Column('genre', String(255), nullable=False)
    words = relationship('Word', backref='word_genres')


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)