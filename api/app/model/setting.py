from os import getenv, path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

print(getenv('DB_DIR_PATH'))

DB_FILE = path.join(getenv('DB_DIR_PATH'), 'simple_game.db')

# DB接続するためのEngineインスタンス
engine = create_engine('sqlite:///' + DB_FILE, echo=True)

# DBに対してORM操作するときに利用
# Sessionを通じて操作を行う
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=True,
        bind=engine)
)

Base = declarative_base()

# 予めテーブル定義の継承元クラスにqueryプロパティを仕込んでおく
Base.query = session.query_property()

