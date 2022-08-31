# FIRST FLASK APP LETS GO!!!

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return'<h1>Hello, World!</h1> <p>Is this working?</p>'

@app.route('/test')
def letsGo():
    return'Failure is not an option'