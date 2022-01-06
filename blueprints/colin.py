from flask import Blueprint, render_template
import requests

bcolin = Blueprint("bcolin", __name__, static_folder="static", template_folder="templates")

@bcolin.route('/colin/')
def colin():
    return render_template('colin.html')

