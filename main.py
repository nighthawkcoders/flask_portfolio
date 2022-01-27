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

from crud.app_crud import app_crud
app.register_blueprint(app_crud)

from database.app_database import app_database
app.register_blueprint(app_database)

from flight.app_flight import app_flight
app.register_blueprint(app_flight)

from crud.app_crud_api import app_crud_api
app.register_blueprint(app_crud_api)

darkmode="darkmode"
# connects default URL to render index.html

@app.route('/')
def index():
    return render_template("index.html", darkmode=darkmode)

@app.route('/places/')
def places():
    return render_template("places.html", darkmode=darkmode)


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
    return render_template("location.html", location=response.json(), darkmode=darkmode)

@app.route('/locations', methods=['GET', 'POST'])
def locations():
    url = "http://127.0.0.1:8081/api/locations"
    response = requests.request("GET", url)
    return render_template("locations.html", locations=response.json(), darkmode=darkmode)

@app.route('/fetchdemo', methods=['GET', 'POST'])
def fetchdemo():
    return render_template("fetchdemo.html", darkmode=darkmode)

@app.route('/darkmode', methods=['GET', 'POST'])
def toggleDarkMode():
    global darkmode
    if darkmode == "darkmode":
        darkmode="lightmode"
    else:
        darkmode = "darkmode"
    print(darkmode)
    return ('', 200)


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True,port=8081)