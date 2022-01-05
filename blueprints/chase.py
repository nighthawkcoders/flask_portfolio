from flask import Blueprint, render_template
import requests
from algorithms.ChaseAPI import game
from algorithms.Table import enclosure, enclosure2

bchase = Blueprint("bchase", __name__, static_folder="static", template_folder="templates")


@bchase.route('/Chase/')
def chase():
    return render_template('Chase.html', fgame=game())


@bchase.route('/cats/')
def cats():
    return render_template('cat.html')


@bchase.route('/Enclosures/')
def Enclosures():
    return render_template('Enclosures.html', enclosure=enclosure(), enclosure2=enclosure2())

