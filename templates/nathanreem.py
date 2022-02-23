from flask import Flask, render_template
from flask import request, Blueprint
from __init__ import app
import requests, random

nathanreem = Blueprint('nathanreem', __name__,
                     url_prefix='/NR',
                     template_folder='templates/',
                     static_folder='static',
                     static_url_path='assets')

numbers = []
avg = 0


@nathanreem.route('/nathanreem', methods=['GET', 'POST'])
def number():
    return render_template("nathanreem.html")