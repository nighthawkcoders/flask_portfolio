# import "packages" from flask
from flask import Blueprint, render_template
import requests
import json
import random

# create a Flask instance
blueprint = Blueprint('blueprint', __name__)

# connects default URL to render index.html
@blueprint.route('/LucasAboutMe/')
def LucasAboutMe():
    url = "https://f1-race-schedule.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-host': "f1-race-schedule.p.rapidapi.com",
        'x-rapidapi-key': "9d1b3b63d7msh7765eaeb56e30d0p1d3c7ejsna149c7e76f59"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    return render_template("LucasAboutMe.html", output=response.json())

@blueprint.route('/IanAboutMe/')
def IanAboutMe():
    return render_template("IanAboutMe.html")


@blueprint.route('/KianAboutMe/')
def KianAboutMe():
    return render_template("KianAboutMe.html")

    url = "https://genius.p.rapidapi.com/artists/16775/songs"

    headers = {
        'x-rapidapi-host': "genius.p.rapidapi.com",
        'x-rapidapi-key': "74bd99649amsha1c396dfa85e888p1c1773jsn35b095711d42"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

@blueprint.route('/GavinAboutMe/')
def GavinAboutMe():
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring = {"r":"json","type":"movie","i":"tt{id}".format(id=random.randint(1000000,4000000))}

    headers = {
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
        'x-rapidapi-key': "7815f70232mshea0c87cc336b4aap13f459jsn464272722115"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    return render_template("GavinAboutMe.html", moviequiz=data)