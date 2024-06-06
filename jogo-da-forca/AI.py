import openai as ai
from dotenv import load_dotenv, find_dotenv
import os
from typing import List


_ = load_dotenv(find_dotenv())

client = ai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def get_prompt(difficulty: str, language: str) -> List:
    return [{'role': 'user',
             'content': f"""Escolha aleatoriamente uma palavra em uma lista de palavras aleatórias 
             para uma rodada do jogo da forca. A Dificuldade da palavra é {difficulty} e o Idioma da palavra é: {language}. 
             Responda SOMENTE com A PALAVRA {difficulty} EM {language}, nada mais, nada menos. exemplo de resposta: 'exemplo'"""}]


def get_word(difficulty: str, language: str, model = 'gpt-3.5-turbo-0125', max_tokens = 100, temperature = 1) -> str:
    """Função para pegar a palavra do GPT

    Args:
        difficulty (str): nível de dificuldade
        language (str): idioma da palavra
        model (str, optional): modelo do GPT. Defaults to 'gpt-3.5-turbo-0125'.
        max_tokens (int, optional): máximo de tokens. Defaults to 100.
        temperature (int, optional): "variedade" das palavras. Defaults to 1.

    Returns:
        str: A palavra gerada.
    """
    response = client.chat.completions.create(
        messages = get_prompt(difficulty, language),
        model = model,
        max_tokens = max_tokens,
        temperature = temperature
        )

    return response.choices[0].message.content
