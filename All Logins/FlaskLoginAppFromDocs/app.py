# link to docs: https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/


# Imports
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')