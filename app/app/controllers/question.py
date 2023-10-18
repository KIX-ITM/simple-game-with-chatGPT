from app.api import fast_api


def get_new_question():
    path = 'questions'
    response = fast_api.get(path)
    return response


def get_question_by_id(id, difficulty):
    path = 'questions/' + id + '/' + difficulty
    response = fast_api.get_with_auth_code(path)
    return response


def format_response(response):
    obj = {}
    obj['question_id'] = response['id'] 
    obj['option_a'] = response['option_a_ja']
    obj['option_b'] = response['option_b_ja']
    obj['option_c'] = response['option_c_ja']
    obj['correct_words'] = [None, None]
    obj['incorrect_word'] = None
    count = 0
    for i in ['a', 'b', 'c']:
        key = 'option_' + i + '_is_common'
        option = 'option_' + i
        if response[key]:
            obj['correct_words'][count] = obj[option]
            count += 1
        if not response[key]:
            obj['incorrect_word'] = obj[option]
    return obj
