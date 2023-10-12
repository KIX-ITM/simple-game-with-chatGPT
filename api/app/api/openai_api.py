import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def request(text):
    response = openai.Completion.create(
      model="gpt-3.5-turbo-instruct",
      prompt=text
    )
    return response

