from flask import Blueprint, render_template
import requests

btanay = Blueprint("btanay", __name__, static_folder="static", template_folder="templates")

@btanay.route('/tanay/', methods=['GET', 'POST'])
def tanay():
    return render_template('tanay.html')

@btanay.route('/hangman/')
def hangman():
    return render_template('hangman.html')