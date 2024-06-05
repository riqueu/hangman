import openai as ai
from dotenv import load_dotenv, find_dotenv
import os
from typing import List


_ = load_dotenv(find_dotenv())

client = ai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def get_prompt(dificuldade: str) -> List:
    return [{"role":"user",
             "content": f"""Escolha aleatoriamente uma palavra em uma lista de palavras aleatórias 
             para uma rodada do jogo da forca. Responda somente com A PALAVRA,
             nada mais, nada menos. A palavra deve a dificuldade: {dificuldade}"""}]


def get_word(dificuldade: str, model = 'gpt-3.5-turbo-0125', max_tokens = 100, temperature = 1) -> str:
    """Função que recebe uma dificuldade e retorna a palavra

    Args:
        dificuldade (str): Dificuldade da palavra para o jogo
        model (str, optional): Modelo do ChatGPT. Defaults to 'gpt-3.5-turbo-0125'.
        max_tokens (int, optional): Máximo de Tokens. Defaults to 100.
        temperature (int, optional): "Diversidade/Aleatoriedade" das palavras. Defaults to 1.

    Returns:
        str: A resposta do GPT (palavra).
    """
    response = client.chat.completions.create(
        messages = get_prompt(dificuldade),
        model = model,
        max_tokens = max_tokens,
        temperature = temperature
        )

    return response.choices[0].message.content
