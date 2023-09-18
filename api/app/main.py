from typing import Union

from fastapi import FastAPI

application = FastAPI()

# テスト用
@application.get("/")
def read_root():
    return {"Hello": "World"}

# テスト用
@application.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}