import openai as ai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = ai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response(prompt, model = "gpt-3.5-turbo-0125", max_tokens = 500, temperature = 0):
    response = client.chat.completions.create(messages = prompt,
                                              model = model,
                                              max_tokens = max_tokens,
                                              temperature = temperature)
    
    # print(response.choices[0].message.content) 
    prompt.append({"role": "assistant", "content": response.choices[0].message.content})
    
    return response