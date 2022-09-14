from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Ain't this Grand?</p>"

@app.route("/<char1>")
def hello_world2(char1):
    return f"<p>Hello, {escape(char1)} Ain't this Grand?</p>"