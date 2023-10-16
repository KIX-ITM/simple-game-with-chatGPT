from app.api import fast_api


def get_new_question():
    path = 'questions'
    response = fast_api.get(path)
    return response


def get_question_by_id(id, difficulty):
    path = 'questions/' + id + '/' + difficulty
    response = fast_api.get_with_auth_code(path)
    return response