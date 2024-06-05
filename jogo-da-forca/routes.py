from flask import render_template, request, redirect, url_for, session
from flask.wrappers import Response
from unidecode import unidecode
import hangman as hg
import AI


def configure_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/difficulty', methods=['GET', 'POST'])
    def chose_difficulty() -> Response:
        if request.method == 'POST':
            difficulty = request.form.get('difficulty')
            session['difficulty'] = difficulty
            
            word = AI.get_word(session['difficulty'])
            session['word'] = hg.to_alpha(word)
            
            session['used_letters'] = ""
            session['vidas'] = 5
            
            session['original_word'] = session['word']
            session['palavra_oculta'] = "_"*len(session['word'])
            return redirect(url_for('game'))
        
        return render_template('difficulty.html')
    

    @app.route('/game', methods=['GET', 'POST'])
    def game() -> Response:
        if 'difficulty' not in session:
            return redirect(url_for("chose_difficulty"))
        
        if request.method == 'POST':
            message = ""
            message_status = ""
            
            letter = request.form.get('letter')
            # Verifica se a letra é valida
            letter = hg.to_alpha(letter)
            
            if len(letter) == 0:
                message = "Entrada invalida!"
                message_status = "error"
            elif letter in session['used_letters']:
                message = "Letra já usada!"
                message_status = "error"
            
            
            
            elif not letter in session['word']:
                session['vidas'] -= 1
                message = "Letra não está na palavra! -1 vida."
                message_status = "bad"
                
            else:
                session['palavra_oculta'], session['word'] = hg.update_word(session['palavra_oculta'], session['word'], letter)
                message = "Letra está na palavra! :)"
                message_status = "good"
            
            session['used_letters'] += letter
            
            if hg.game_state(session['palavra_oculta'], session['vidas']):
                return redirect(url_for(hg.game_state(session['palavra_oculta'], session['vidas'])))
            
            return render_template('game.html', message = message, message_status = message_status)
        
        return render_template('game.html')
    