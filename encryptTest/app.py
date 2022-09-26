# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import os
from turtle import title
from flask import Flask, flash, request, redirect, url_for, render_template,send_from_directory
from werkzeug.utils import secure_filename
from markupsafe import escape

from cryptography.fernet import Fernet


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Making Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-




# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Flask Routes
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
app = Flask(__name__)


# downloading a file from python (url will be 127.0.0.1/filenameToDownload.extension)
DOWNLOAD_DIRECTORY = "./UPLOADS"

@app.route("/<path:path>",methods = ['GET','POST'])
def hello_world(path):
    try:
        return send_from_directory(DOWNLOAD_DIRECTORY,path,as_attachment=True)
            #"<p>Hello, World! Ain't this Grand? I THINK SO!</p>"
    except FileNotFoundError:
        os.abort(404)
#all i need to do is to have the original url redirect to another route with the filename at the end and we have liftoff
#can use datetime to generate unique number for this to make it harder for people to download things (and have it stored in a completely seperate downloads folder)

"""
@app.route("/")
def hello_world():
    title = "This is the title"
    if request.method == 'POST':
        file = request.files['file']
            # Filename below - Important for functions 
        filename = "toDownload.jpg"
        file.send(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return "<p>Hello, World! Ain't this Grand? I THINK SO!</p>"
"""
