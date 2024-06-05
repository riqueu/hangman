import openai as ai
from dotenv import load_dotenv, find_dotenv

import os


_ = load_dotenv(find_dotenv())

client = ai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_response(prompt, model = 'gpt-3.5-turbo-0125', max_tokens = 500, temperature = 0):
    response = client.chat.completions.create(
        messages = prompt,
        model = model,
        max_tokens = max_tokens,
        temperature = temperature
        )

    return response.choices[0].message.content
