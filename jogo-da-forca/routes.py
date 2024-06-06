from flask import render_template, request, redirect, url_for, session
from flask.wrappers import Response
import hangman as hg
import AI


def configure_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/difficulty', methods=['GET', 'POST'])
    def chose_difficulty() -> Response:
        if request.method == 'POST':
            difficulty = request.form.get('difficulty')
            session['difficulty'] = difficulty
            return redirect(url_for('language'))
        
        return render_template('difficulty.html')
    
    
    @app.route('/language', methods=['GET', 'POST'])
    def language() -> Response:
        if request.method == 'POST':
            language = request.form.get('language')
            session['language'] = language
            word = AI.get_word(session['difficulty'], session['language'])
            session['word'] = hg.to_alpha(word)
            
            session['used_letters'] = ''
            session['lives'] = 5
            
            session['original_word'] = session['word']
            session['hidden_word'] = '_'*len(session['word'])
            return redirect(url_for('game'))
        
        
        return render_template('language.html')


    @app.route('/game', methods=['GET', 'POST'])
    def game() -> Response:
        if not session['difficulty']:
            return redirect(url_for('chose_difficulty'))
        
        if request.method == 'POST':
            message = ''
            message_status = ''
            
            letter = request.form.get('letter')
            # Verifica se a letra é valida
            letter = hg.to_alpha(letter)
            
            if len(letter) == 0:
                message = 'Entrada invalida!'
                message_status = 'error'

            elif letter in session['used_letters']:
                message = 'Letra já usada!'
                message_status = 'error'
            
            elif letter not in session['word']:
                session['lives'] -= 1
                message = 'Letra não está na palavra! -1 vida.'
                message_status = 'bad'
                
            else:
                session['hidden_word'], session['word'] = hg.update_word(session['hidden_word'], session['word'], letter)
                message = 'Letra está na palavra! :)'
                message_status = 'good'
            
            if letter not in session['used_letters']:
                session['used_letters'] += letter
            
            if hg.game_state(session['hidden_word'], session['lives']):
                return redirect(url_for(hg.game_state(session['hidden_word'], session['lives'])))
            
            return render_template('game.html', message = message, message_status = message_status)
        
        return render_template('game.html')
    

    @app.route('/win', methods=['GET', 'POST'])
    def win() -> Response:
        if not session['difficulty']:
            return redirect(url_for('chose_difficulty'))
        
        if '_' in session['hidden_word']:
            return redirect(url_for('game'))

        if request.method == 'POST':
            session.clear()
            return redirect(url_for('chose_difficulty'))
        return render_template('win.html')
    
    @app.route('/lose', methods=['GET', 'POST'])
    def lose() -> Response:
        if not session['difficulty']:
            return redirect(url_for('chose_difficulty'))
        
        if request.method == 'POST':
            session.clear()
            return redirect(url_for('chose_difficulty'))
        return render_template('lose.html')
