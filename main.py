# import "packages" from flask

from flask import render_template, request
from __init__ import app
import requests
import json

from templates.about import about_pg
app.register_blueprint(about_pg)

from api.webapi import api_bp
app.register_blueprint(api_bp)

from algorithm.algorithm import app_algorithm
app.register_blueprint(app_algorithm)

from crud.app_crud import app_crud
app.register_blueprint(app_crud)

darkmode="darkmode"
# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html", darkmode=darkmode)

@app.route('/places/')
def places():
    return render_template("places.html", darkmode=darkmode)

@app.route('/jason/')
def jason():
    url = "https://video-game-news.p.rapidapi.com/star_wars"

    headers = {
        'x-rapidapi-host': "video-game-news.p.rapidapi.com",
        'x-rapidapi-key': "9c2bef1841msh474f0e89d12625ap15b46cjsn29537babe185"
    }

    response = requests.request("GET", url, headers=headers)

    final=response.text
    return render_template("aboutpages/jason.html", darkmode=darkmode)


@app.route('/adi', methods={'GET', 'POST'})
def adi():
    url = "https://sportscore1.p.rapidapi.com/sports/1/teams"
    headers = {
        'x-rapidapi-host': "sportscore1.p.rapidapi.com",
        'x-rapidapi-key': "39c4bf8c2emsh30b02ab6dc01dd9p13f427jsn690a650cf2ec"
    }

    response = requests.request("GET", url, headers=headers)
    return render_template("aboutpages/adi.html", stats=response.json(), darkmode=darkmode)

@app.route('/brian')
def brian():
    # url = "https://tennis-live-data.p.rapidapi.com/tournaments/ATP/2020"
    # headers = {
    #     'x-rapidapi-host': "tennis-live-data.p.rapidapi.com",
    #     'x-rapidapi-key': "3d43659d98msh26d5e705bc7d8b6p1d6431jsnba44357aaf20"
    # }
    # response = requests.request("GET", url, headers=headers)
    # results = json.loads(response.content.decode("utf-8"))['results']
    return render_template("aboutpages/brian.html", darkmode=darkmode)#, res=results)

@app.route('/divya')
def divya():
    url = "https://famous-quotes4.p.rapidapi.com/random"
    querystring = {"category":"all","count":"2"}
    headers = {
        'x-rapidapi-host': "famous-quotes4.p.rapidapi.com",
        'x-rapidapi-key': "80afb5b6afmsh552d92e769ba3a5p1bfac9jsnfb6c407dd20f"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    quotes = []
    for result in response:
        quotes.append(result['text'] + " by author: " + result['author'])
    return render_template("aboutpages/divya.html", quotes=quotes, darkmode=darkmode)

@app.route('/rohan', methods=['GET', 'POST'])
def rohan():
    url = "https://free-nba.p.rapidapi.com/players"

    headers = {
       'x-rapidapi-host': "free-nba.p.rapidapi.com",
        'x-rapidapi-key': "35a01f5f74msh20628303ae6dbefp168484jsn83f86e2f8568"
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return render_template("aboutpages/rohan.html", data=data, darkmode=darkmode)

@app.route('/photogallery', methods=['GET', 'POST'])
def photogallery():
    if request.form:
        input = request.form.get("input")
        if len(input) != 0:
            return render_template("photogallery.html", input1=input, darkmode=darkmode)
    return render_template("pbl/photogallery.html", input1="", darkmode=darkmode)

@app.route('/weather/', methods=['GET','POST'])
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

@app.route('/hotels/', methods=['GET','POST'])
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




@app.route('/carrental', methods=['GET', 'POST'])
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

@app.route('/flights', methods=['GET', 'POST'])
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


@app.route('/maps', methods=['GET', 'POST'])
def maps():

    return render_template("pbl/maps.html", darkmode=darkmode)

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

@app.route('/darkmode', methods=['GET', 'POST'])
def toggleDarkMode():
    global darkmode
    if darkmode=="darkmode":
        darkmode="lightmode"
    else:
        darkmode="darkmode"
    return ('', 200)



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True,port=8081)