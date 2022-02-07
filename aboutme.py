from flask import Blueprint, render_template, app

app_aboutme = Blueprint('aboutme', __name__)

@app_aboutme.route('/mainabout/')
def mainabout():
    return render_template("mainabout.html")

@app_aboutme.route('/aboutnathan')
def aboutnathan():
    return render_template("aboutnathan.html")


@app_aboutme.route('/aboutreem')
def aboutreem():
    return render_template("aboutreem.html")


@app_aboutme.route('/aboutjacob')
def aboutjacob():
    return render_template("aboutjacob.html")


@app_aboutme.route('/aboutjames')
def aboutjames():
    return render_template("aboutjames.html")


@app_aboutme.route('/aboutdaniel')
def aboutdaniel():
    return render_template("aboutdaniel.html")
