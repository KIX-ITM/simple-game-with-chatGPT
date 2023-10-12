from api import openai_api

DIFFICULTY_DICT = {'easy':'10 words', 'normal':'5 words', 'hard':'1 word'}
OPTION_NAMES = ['option_a', 'option_b', 'option_c']


def request(optipns, difficulty):
    text = create_prompt(optipns, difficulty)
    if text:
        response = openai_api.request(text)
        common_point = response['choices'][0]['text']
        return common_point.replace('\n', '')
    else:
        return False


def create_prompt(question_data, difficulty):
    data = question_data.__dict__
    common_words = []
    if difficulty in DIFFICULTY_DICT:
        word_num = DIFFICULTY_DICT[difficulty]
        for name in OPTION_NAMES:
            cond = data[name + '_is_common']
            word = data[name + '_en']
            if cond : common_words.append(word)
            if not cond : other_word = word
        return insert_words(common_words, other_word, word_num)
    return False


def insert_words(common_words, other_word, word_num):
    prompt = [
                'There are three words: "',
                common_words[0], '", "',
                common_words[1], '", "',
                other_word, '". ',
                'Describe in of ', word_num,
                ' what only "',
                common_words[0], '" and "',
                common_words[1], '" have in common. ',
                'Do not use the words "',
                common_words[0], '" and "',
                common_words[1], '".',
    ]
    return ''.join(prompt)
