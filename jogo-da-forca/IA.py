import openai as ai
from dotenv import load_dotenv, find_dotenv
import os
from unidecode import unidecode
from typing import List

_ = load_dotenv(find_dotenv())

client = ai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def get_prompt(dificuldade: str) -> List:
    prompt = [{"role":"user",
               "content": f"""Escolha aleatoriamente uma palavra para uma rodada do jogo da forca. 
               Responda somente com A PALAVRA, nada mais, nada menos. 
               A palavra deve a dificuldade: {dificuldade}"""}]
    return prompt


def get_word(dificuldade: str, model = 'gpt-3.5-turbo-0125', max_tokens = 100, temperature = 1) -> str:
    """Função que recebe uma dificuldade e retorna a palavra

    Args:
        dificuldade (str): Dificuldade da palavra para o jogo
        model (str, optional): Modelo do ChatGPT. Defaults to 'gpt-3.5-turbo-0125'.
        max_tokens (int, optional): Máximo de Tokens. Defaults to 100.
        temperature (int, optional): "Diversidade/Aleatoriedade" das palavras. Defaults to 1.

    Returns:
        str: A palavra maiúscula e tratada para o jogo.
    """
    response = client.chat.completions.create(
        messages = get_prompt(dificuldade),
        model = model,
        max_tokens = max_tokens,
        temperature = temperature
        )

    # Tratamento da palavra (maiúscula, só alfabéticos, sem acentuação, etc)
    palavra = response.choices[0].message.content.upper()
    palavra = "".join(filter(str.isalpha, palavra))
    return unidecode(palavra)
