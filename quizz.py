# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 12:11:26 2021

@author: Morgane
"""

# For the API Flask
from flask import Flask
import random
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


@app.route('/newquestion')
def new_question():
    return jsonify(generator.new_question())


"""
@app.route('/', methods=['POST'])
def start():
    print("Start the quiz")
    #return render_template("rules.html") #A changer --> on crée une autre page pour les questions ?
    name="coucou"
    return name
"""

'''_______________________________________QUERIES_______________________________________'''

'''_______________________________________MAIN_______________________________________'''

if __name__ == "__main__":
    # Launch our Website
    print("\nLaunch :")
    app.run()
