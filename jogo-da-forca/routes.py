from flask import render_template, request, redirect, url_for, session
from flask.wrappers import Response


def configure_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/difficulty', methods=['GET', 'POST'])
    def chose_difficulty() -> Response:
        if request.method == 'POST':
            difficulty = request.form.get('difficulty')
            session['difficulty'] = difficulty
            return redirect(url_for(game))
        
        return render_template('difficulty.html')
    

    @app.route('/', methods=['GET', 'POST'])
    def game() -> Response:
        pass
