from unidecode import unidecode

def to_alpha(string: str):
    return unidecode(''.join(filter(str.isalpha, string)).upper())

def update_word(hidden_word, word, letter):
    for index in range(len(word)):
        # Para cada letra, verifica se eh a letra procurada
        if word[index] == letter:
            # Se sim, substitui na palavra oculta
            hidden_word = hidden_word[:index] + letter + hidden_word[(index + 1):]
            #Retira da palavra a letra encontrada
            word = word[:index] + '_' + word[(index + 1):]
    return hidden_word, word

def game_state(hidden_word, lives):
    if '_' not in hidden_word:
        return 'win'
    elif lives == 0:
        return 'lose'
    # jogo segue
    return False
  