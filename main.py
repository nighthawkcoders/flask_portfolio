# import "packages" from flask

from flask import render_template, request
from __init__ import app
import requests
import json

from templates.travel import travel_pg
app.register_blueprint(travel_pg)

from templates.about import about_pg
app.register_blueprint(about_pg)

from api.webapi import api_bp
app.register_blueprint(api_bp)

from algorithm.algorithm import app_algorithm
app.register_blueprint(app_algorithm)

from sc_crud.app_crud import app_crud
app.register_blueprint(app_crud)

from database.app_database import app_database
app.register_blueprint(app_database)

from flight.app_flight import app_flight
app.register_blueprint(app_flight)

from page.app_page import app_page
app.register_blueprint(app_page)

from sc_crud.app_crud_api import app_crud_api
app.register_blueprint(app_crud_api)

darkmode="darkmode"

tictactoearray=[["","",""],["","",""],["","",""]]
# connects default URL to render index.html

@app.route('/')
def index():
    return render_template("index.html", darkmode=darkmode)

@app.route('/navbarsearch', methods=['GET', 'POST'])
def navbarsearch():
    if request.form:
        term = request.form.get("term")
        if len(term) != 0:
            return render_template("navbarsearch.html", navbarsearch=term, darkmode=darkmode)

@app.route('/searchtest/')
def searchtest():
    return render_template("searchtest.html", darkmode=darkmode)

@app.route('/photogallery', methods=['GET', 'POST'])
def photogallery():
    if request.form:
        input = request.form.get("input")
        if len(input) != 0:
            return render_template("pbl/photogallery.html", input1=input, darkmode=darkmode)
    return render_template("pbl/photogallery.html", input1="", darkmode=darkmode)

@app.route('/location', methods=['GET', 'POST'])
def location():
    url = "http://127.0.0.1:8081/api/location"
    response = requests.request("GET", url)
    return render_template("pbl/location.html", location=response.json(), darkmode=darkmode)

@app.route('/locations', methods=['GET', 'POST'])
def locations():
    url = "http://127.0.0.1:8081/api/locations"
    response = requests.request("GET", url)
    return render_template("pbl/locations.html", locations=response.json(), darkmode=darkmode)

@app.route('/fetchdemo', methods=['GET', 'POST'])
def fetchdemo():
    return render_template("pbl/fetchdemo.html", darkmode=darkmode)

@app.route('/minigames', methods=['GET', 'POST'])
def minigames():
    if request.form:
        word1 = request.form.get("word1")
        word2 = request.form.get("word2")
        if len(word1) < len(word2):
            shorterlen = len(word1)
            difference = len(word2) - len(word1)
        else:
            shorterlen = len(word2)
            difference = len(word1) - len(word2)
        for x in range(0, shorterlen):
            if word1[x] != word2[x]:
                difference += 1
        return render_template("pbl/minigames.html", result=difference, darkmode=darkmode)
    return render_template("pbl/minigames.html", darkmode=darkmode)

@app.route('/darkmode', methods=['GET', 'POST'])
def toggleDarkMode():
    global darkmode
    if darkmode == "darkmode":
        darkmode="lightmode"
    else:
        darkmode = "darkmode"
    print(darkmode)
    return ('', 200)

@app.route('/travelchecklist/')
def travelchecklist():
    return render_template("pbl/travelchecklist.html", darkmode=darkmode)

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True, port=8081)
