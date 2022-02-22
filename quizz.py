# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 12:11:26 2021

@author: Morgane
"""

# For the API Flask
from flask import Flask
from flask import render_template, jsonify
from question_generator.question_generator import QuestionGenerator
from flask import request

'''_______________________________________APP FLASK_______________________________________'''

app = Flask(__name__, template_folder="templates")

app.config["SECRET_KEY"] = "alexandremorgane"

app = Flask(__name__)

generator = QuestionGenerator()


# default
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index.html')
def play():
    return render_template('index.html')


@app.route('/rules.html')
def rules():
    return render_template('rules.html')

@app.route('/index_french.html')
def play_french():
    return render_template('index_french.html')


@app.route('/rules_french.html')
def rules_french():
    return render_template('rules_french.html')


@app.route('/newquestion')
def new_question():
    theme = request.args.get('theme')
    language = request.args.get('language')
    return jsonify(generator.new_question(theme,language))


'''_______________________________________MAIN_______________________________________'''

if __name__ == "__main__":
    # Launch our Website
    print("\nLaunch :")
    app.run()
