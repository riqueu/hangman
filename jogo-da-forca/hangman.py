from flask import session
from unidecode import unidecode

def to_alpha(string: str):
    return unidecode("".join(filter(str.isalpha, string)).upper())
