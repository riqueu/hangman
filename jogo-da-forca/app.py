from flask import Flask
from routes import configure_routes

app = Flask(__name__)

app.secret_key = 'c>python'

configure_routes(app)

if __name__ == '__main__':
    app.run(debug=False)
