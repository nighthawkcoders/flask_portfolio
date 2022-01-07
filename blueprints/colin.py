from flask import Blueprint, render_template
import requests

bcolin = Blueprint("bcolin", __name__, static_folder="static", template_folder="templates")

@bcolin.route('/colin/')
def colin():


@bcolin.route('/imageCarousel/')
def imageCarousel():
    return render_template('PBL Pages/imageCarousel.html')
