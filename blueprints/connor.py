from flask import Blueprint, render_template
import requests

bconnor = Blueprint("bconnor", __name__, static_folder="static", template_folder="templates")

@bconnor.route('/connor/')
def connor():
    return render_template('connor.html')