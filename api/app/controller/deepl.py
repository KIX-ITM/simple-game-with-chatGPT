from app.api import deepl_api


def request(text):
    response = deepl_api.request(text)
    return response