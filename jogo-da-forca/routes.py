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
            session["used_letters"] = set()
            word = AI.get_word(session['difficulty'])
            session["word"] = hg.to_alpha(word)
            return redirect(url_for("game"))
        
        return render_template('difficulty.html')
    

    @app.route('/game', methods=['GET', 'POST'])
    def game() -> Response:
        if "difficulty" not in session:
            return redirect(url_for("chose_difficulty"))
        
        
        if request.method == 'POST':
            letter = request.form.get('letter')
            # Verifica se a letra é valida
            if len(hg.to_alpha(letter)) == 0:
                return render_template('game.html', message = "Entrada invalida!")
            if hg.to_alpha(letter) in session["used_letters"]:
                return render_template('game.html', message = "Letra já usada!")
            session['letter'] = letter
            
            
            
            
            
            
            return redirect(url_for("game"))
        
        
        return render_template('game.html')
    
