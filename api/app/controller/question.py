import random


def create_three_option(words, genres):
    word_list = []
    for word in words:
        word_list.append([word.japanese, word.english, word.genre_id])

    genre_list = []
    for genres in genres:
        genre_list.append(genres.id)

    bool_list = [True, True, False]
    random_bool_list = select_all_at_random(bool_list)
    three_genres = select_three_at_random(genre_list)
    count = 0

    result = []

    for genre in three_genres:
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


