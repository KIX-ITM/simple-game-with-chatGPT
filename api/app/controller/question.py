import random

from app.model import crud


def exists_common_point(question_data, difficulty):
    if difficulty == 'easy' and question_data.easy_common_point_ja:
        return True
    if difficulty == 'normal'and question_data.normal_common_point_ja:
        return True
    if difficulty == 'hard' and question_data.hard_common_point_ja:
        return True
    return False


def update_common_point(db, id, difficulty, en, ja):
    crud.update_common_point(db, id, difficulty, en, ja)
    return get_one_question(db, id)


def get_one_question(db, id):
    return crud.get_question(db, question_id=id)


def create_options(db):
    words = crud.get_all_words(db)
    genres = crud.get_all_genre_id(db)
    options = create_three_options(words, genres)
    insert_data = create_question_dict(options)
    return crud.create_question(db, question=insert_data)


def create_question_dict(arr):
    option_a = arr[0]
    option_b = arr[1]
    option_c = arr[2]
    new_dict = dict(
    option_a_ja=option_a['japanese'],
    option_b_ja=option_b['japanese'],
    option_c_ja=option_c['japanese'],
    option_a_en=option_a['english'],
    option_b_en=option_b['english'],
    option_c_en=option_c['english'],
    option_a_is_common=option_a['is_common'],
    option_b_is_common=option_b['is_common'],
    option_c_is_common=option_c['is_common']
    )
    return new_dict


def create_three_options(words, genres):
    word_list = []
    for word in words:
        word_list.append([word.japanese, word.english, word.genre_id])

    genre_list = []
    for genres in genres:
        genre_list.append(genres.id)

    bool_list = [True, True, False]
    random_bool_list = select_all_at_random(bool_list)
    three_genres = select_three_at_random(genre_list)
    # genre = select_one_at_random(genre_list)
    count = 0

    result = []

    for genre in three_genres:
    # for i in range(3):
        obj = select_one_word_at_random(word_list, genre, random_bool_list[count])
        result.append(obj)
        count += 1

    return result


def select_one_word_at_random(word_list, genre, cond):
    new_word_list = [i for i in word_list if i[2] == genre]
    word = select_one_at_random(new_word_list)
    obj = {
        'japanese': word[0],
        'english': word[1],
        'is_common': cond
    }
    return obj


def select_three_at_random(data):
    return random.sample(data, 3)


def select_one_at_random(data):
    result = random.sample(data, 1)
    return result[0]


def select_all_at_random(data):
    return random.sample(data, len(data))





