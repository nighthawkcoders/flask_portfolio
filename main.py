# import "packages" from flask
from flask import Flask, render_template
import requests
import json
import random
from crud.app_crud import app_crud
from aboutus import aboutus

# create a Flask instance
from __init__ import app

app.register_blueprint(app_crud)
app.register_blueprint(aboutus)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/darktest/')
def darktest():
    return render_template("about_us/darktest.html")

@app.route("/final_grade_calc/")
def final_grade_calc():
    return render_template("final_grade_calc.html")
@app.route('/apec/')
def apec():
    return render_template("subjects/apec.html")

@app.route('/apush/')
def apush():
    return render_template("subjects/apush.html")

@app.route('/biology/')
def biology():
    return render_template("subjects/biology.html")

@app.route('/calcab/')
def calcab():
    return render_template("subjects/calcab.html")

@app.route('/chemistry/')
def chemisty():
    return render_template("subjects/chemistry.html")

@app.route('/csp/')
def csp():
    return render_template("subjects/csp.html")

@app.route('/stats/')
def stats():
    return render_template("subjects/stats.html")

@app.route('/notes/')
def notes():
    return render_template("subjects/notes.html")
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# runs the application on the development server
@app.route('/flashcards/')
def flashcards():
    return render_template('flashcards.html')

if __name__ == "__main__":
    app.run(debug=True, port="5002")
