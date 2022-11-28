# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from flask import Flask, flash, request, redirect, url_for, render_template,send_from_directory, jsonify
import os
from os import path
import datetime
from pydub import AudioSegment
import speech_recognition as sr
import librosa
import soundfile as sf
import wave
from deep_translator import MyMemoryTranslator
import json
from gtts import gTTS
from pathlib import Path


app = Flask(__name__)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Routes
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
@app.route('/',methods=['GET', 'POST'])
def mainIndex():
    dashboardHeader = "Speech to Speech" # in base temp, basically what this page does
    title = "Speech to Speech - Jacob Clouse Universal Translator" # in base temp, actual page title in browser
    returned_translated = "Translated text will display here"
    return render_template('translate.html', html_title = title, dash_head = dashboardHeader, translated = returned_translated)

@app.route('/audioUpload',methods=['GET','POST'])
def translate():
    if request.method == "POST":
        memory = "newMem!"
    
    if request.method == "GET":
        memory = "this was a get"
    # return render_template('translate.html', html_title = title, dash_head = dashboardHeader, translated = returned_translated)
    return redirect(url_for("altMain", memory = memory))


@app.route('/alt',methods=['GET', 'POST'])
def altMain():
    dashboardHeader = "Alt Main" # in base temp, basically what this page does
    title = "Speech to Speech - Jacob Clouse Universal Translator" # in base temp, actual page title in browser
    returned_translated = request.args.get('memory')
# return render_template('translate.html', html_title = title, dash_head = dashboardHeader)
    return render_template('translate.html', html_title = title, dash_head = dashboardHeader, translated = returned_translated)


@app.route ('/redirect',methods=['GET', 'POST'])
def myRedirect():

    return redirect(url_for("translate"))


# main statement - used to set dev mode
if __name__ == '__main__':
    app.run(debug=True)



