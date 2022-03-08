from flask import Flask, render_template
from flask import request, Blueprint
from __init__ import app
import requests, random

jacobgame = Blueprint('jacobgame', __name__,
                       url_prefix='/JG',
                       template_folder='templates/',
                       static_folder='static',
                       static_url_path='assets')


@jacobgame.route('/jacobgame', methods=['GET', 'POST'])
def number():
    return render_template("jacobgame.html")