from flask import Blueprint, render_template
import requests

btanay = Blueprint("btanay", __name__, static_folder="static", template_folder="templates")

@btanay.route('/tanay/', methods=['GET', 'POST'])
def tanay():
    return render_template('tanay.html')

@btanay.route('/hangman/')
def hangman():
    return render_template('hangman.html')

@btanay.route('/pethistory/')
def pethistory():
    return render_template('pethistory.html')

@btanay.route('/petpoll/')
def petpoll():
    return render_template('petpoll.html')

@btanay.route('/costcalculator/')
def costcalculator():
    return render_template('costcalculator.html')

@btanay.route('/todo/')
def todo():
    return render_template('todo.html')