from flask import Flask, render_template
from flask import request, Blueprint
from __init__ import app
import requests, random

snakegame = Blueprint('snakegame', __name__,
                      url_prefix='/SG',
                      template_folder='templates/',
                      static_folder='static',
                      static_url_path='assets')


@snakegame.route('/snakegame', methods=['GET', 'POST'])
def number():
    return render_template("snakegame.html")