from flask import Blueprint, render_template
import requests
from algorithms.petinfo import pinfo
from pathlib import Path

bconnor = Blueprint("bconnor", __name__, static_folder="static", template_folder="templates")

@bconnor.route('/connor/')
def connor():
    return render_template('connor.html')


@bconnor.route('/PetInfo/')
def PetInfo():
    path = Path(bconnor.root_path) / "testconnorimages"
    return render_template('PetInfo.html', pimage=pinfo(path))