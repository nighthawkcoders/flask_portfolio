from flask import Flask, render_template
from flask import request, Blueprint
from __init__ import app
import requests, random

james = Blueprint('james', __name__,
                       url_prefix='/JL',
                       template_folder='templates/',
                       static_folder='static',
                       static_url_path='assets')


@james.route('/james', methods=['GET', 'POST'])
def number():
    return render_template("james.html")