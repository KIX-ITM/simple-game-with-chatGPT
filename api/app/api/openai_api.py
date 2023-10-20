import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def request(text):
    try:
        response = openai.Completion.create(
          model="gpt-3.5-turbo-instruct",
          prompt=text
        )
        return response
    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        return False
    except openai.error.APIConnectionError as e:
        # Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        return False
    except openai.error.RateLimitError as e:
        # Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        return False
