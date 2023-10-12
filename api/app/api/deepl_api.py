import os
import deepl

auth_key = os.getenv("DEEPL_API_KEY")


def request(text):
    translator = deepl.Translator(auth_key)
    result = translator.translate_text(text, target_lang="JA")
    return result.text