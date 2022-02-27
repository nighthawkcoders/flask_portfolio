from flask import Flask, render_template
from flask import request, Blueprint
from __init__ import app
import requests, random

jacob = Blueprint('jacob', __name__,
                       url_prefix='/JR',
                       template_folder='templates/',
                       static_folder='static',
                       static_url_path='assets')


@jacob.route('/jacob', methods=['GET', 'POST'])
def number():
    return render_template("jacob.html")