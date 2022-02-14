from flask import Flask, Blueprint, render_template, request
import requests
from __init__ import app
import json

about_pages = Blueprint('aboutpages', __name__,
                        url_prefix='/ap',
                        template_folder='templates',
                        static_folder='static', static_url_path='static/aboutpages')

@about_pages.route('/aboutnathan')
def aboutnathan():
    return render_template("aboutnathan.html")

@about_pages.route('/aboutreem')
def aboutreem():
    return render_template("aboutreem.html")


@about_pages.route('/aboutjacob')
def aboutjacob():
    return render_template("aboutjacob.html")


@about_pages.route('/aboutjames')
def aboutjames():
    return render_template("aboutjames.html")


@about_pages.route('/aboutdaniel')
def aboutdaniel():
    return render_template("aboutdaniel.html")

@about_pages.route('/mainabout/')
def mainabout():
    return render_template("mainabout.html")