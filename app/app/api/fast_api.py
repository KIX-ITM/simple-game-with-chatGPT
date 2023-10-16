import os
import json
import requests

URL_HEAD = 'http://127.0.0.9:8000/'
AUTH_CODE = os.getenv('FASTAPI_AUTH_KEY')


def get(path):
    url = URL_HEAD + path
    response = requests.get(url)
    return get_response_detail(response)


def get_with_auth_code(path):
    headers = {'Authorization-Code': AUTH_CODE}
    url = URL_HEAD + path
    response = requests.get(url, headers=headers)
    return get_response_detail(response)


def get_response_detail(response):
    if response.status_code == 200:
        return response.json()
    else:
        return False
