from flask import session
from unidecode import unidecode

def to_alpha(string: str):
    return unidecode("".join(filter(str.isalpha, string)).upper())

def update_word(palavra_oculta, word, letter):
    for index in range(len(word)):
        # Para cada letra, verifica se eh a letra procurada
        if word[index] == letter:
            # Se sim, substitui na palavra oculta
            palavra_oculta = palavra_oculta[:index] + letter + palavra_oculta[(index + 1):]
            #Retira da palavra a letra encontrada
            word = word[:index] + "_" + word[(index + 1):]
    return palavra_oculta, word

def game_state(palavra_oculta, vidas):
    if "_" not in palavra_oculta:
        return "win"
    elif vidas == 0:
        return "lose"
    return False
    
        