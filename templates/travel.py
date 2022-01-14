from flask import Flask, Blueprint, render_template, request
import requests
from __init__ import app
import json

travel_pg = Blueprint('travel', __name__,
                     url_prefix='/travel',
                     template_folder='templates',
                     static_folder='static', static_url_path='static/travel')


darkmode="darkmode"
# connects default URL to render index.html

@travel_pg.route('/places/')
def places():
    return render_template("places.html", darkmode=darkmode)

@travel_pg.route('/weather/', methods=['GET','POST'])
def weather():
    try:
        keyword = request.form['keyword']
    except:
        keyword = ""
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location":keyword,"format":"json","u":"f"}

    headers = {
        'x-rapidapi-host': "yahoo-weather5.p.rapidapi.com",
        'x-rapidapi-key': "3d43659d98msh26d5e705bc7d8b6p1d6431jsnba44357aaf20"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code<400:
        results = json.loads(response.content.decode("utf-8"))
        return render_template("pbl/weather.html", results=results, darkmode=darkmode)
    else:
        return render_template("pbl/weather.html", darkmode=darkmode)

@travel_pg.route('/hotels/', methods=['GET','POST'])
def hotels():
    try:
        keyword = request.form['keyword']
    except:
        keyword = "new york"
    url = "https://hotels4.p.rapidapi.com/locations/v2/search"

    querystring = {"query":keyword,"locale":"en_US","currency":"USD"}

    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': "3d43659d98msh26d5e705bc7d8b6p1d6431jsnba44357aaf20"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(json.loads(response.content.decode("utf-8")))
    results = json.loads(response.content.decode("utf-8"))
    # print(results['suggestions'])
    for suggestions in results['suggestions']:
        # print(suggestions['entities'])
        for entities in suggestions['entities']:
            print(entities['name'])
    return render_template("pbl/hotels.html", results=results, darkmode=darkmode)




@travel_pg.route('/carrental', methods=['GET', 'POST'])
def carrental():

    url = "https://booking-com.p.rapidapi.com/v1/car-rental/search"

    querystring = {"pick_up_datetime":"2022-07-01 13:00:00","pick_up_longitude":"37.620230899","drop_off_longitude":"37.620230899","pick_up_latitude":"55.7518540820001","drop_off_latitude":"55.7518540820001","sort_by":"recommended","locale":"en-gb","currency":"AED","drop_off_datetime":"2022-07-02 13:00:00","from_country":"it"}

    headers = {
        'x-rapidapi-host': "booking-com.p.rapidapi.com",
        'x-rapidapi-key': "2deba3c7c5msh59e591f91803406p14659ajsn14474595701e"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return render_template("pbl/carrental.html", darkmode=darkmode)

@travel_pg.route('/flights', methods=['GET', 'POST'])
def flights():
    url = "https://priceline-com.p.rapidapi.com/flights/LAX/SFO/2021-02-17"

    querystring = {"adults":"1"}

    headers = {
        'x-rapidapi-host': "priceline-com.p.rapidapi.com",
        'x-rapidapi-key': "2deba3c7c5msh59e591f91803406p14659ajsn14474595701e"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return render_template("pbl/flights.html", darkmode=darkmode)


@travel_pg.route('/maps', methods=['GET', 'POST'])
def maps():

    return render_template("pbl/maps.html", darkmode=darkmode)