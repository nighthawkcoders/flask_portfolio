# import "packages" from flask
from flask import Flask, render_template
import requests
import json

# create a Flask instance
app = Flask(__name__)
import random

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")



@app.route('/LucasAboutMe/')
def LucasAboutMe():
    url = "https://f1-race-schedule.p.rapidapi.com/api"
    headers = {
    'x-rapidapi-host': "f1-race-schedule.p.rapidapi.com",
    'x-rapidapi-key': "9d1b3b63d7msh7765eaeb56e30d0p1d3c7ejsna149c7e76f59"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    return render_template("LucasAboutMe.html", output=response.json())

@app.route('/IanAboutMe/')
def IanAboutMe():
    return render_template("IanAboutMe.html")

@app.route('/FunkoPops/')
def funko_pop():
    return render_template("funko_pop.html")


@app.route('/KianAboutMe/')
def KianAboutMe():
    return render_template("KianAboutMe.html")

    url = "https://genius.p.rapidapi.com/artists/16775/songs"

    headers = {
        'x-rapidapi-host': "genius.p.rapidapi.com",
        'x-rapidapi-key': "74bd99649amsha1c396dfa85e888p1c1773jsn35b095711d42"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

@app.route('/GavinAboutMe/')
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


@app.route('/pokemoncards/')
def pokemon_cards():
    url = "https://pokemon-tcg-card-prices.p.rapidapi.com/card"

    querystring = {"setId":"33ee55f4-30d0-4900-850f-36a351fb9719","set":"vivid-voltage","series":"sword-and-shield"}

    headers = {
        'x-rapidapi-host': "pokemon-tcg-card-prices.p.rapidapi.com",
        'x-rapidapi-key': "7815f70232mshea0c87cc336b4aap13f459jsn464272722115"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    return render_template("pokemon_cards.html", pokemoncard=data)


@app.route('/sportscards/')
def sports_cards():
    return render_template("sports_cards.html")


@app.route('/funkopops/')
def funko_pops():
    return render_template("funko_pops.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)


