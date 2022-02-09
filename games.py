from flask import Blueprint, render_template, app, request
import requests

app_games = Blueprint('games', __name__)

@app_games.route('/numberguess', methods=['GET', 'POST'])
def numberguess():
    return render_template("numberguess.html")

@app_games.route('/games')
def games():
    return render_template("games.html")

@app_games.route('/graph')
def graph():
    return render_template("graph.html")