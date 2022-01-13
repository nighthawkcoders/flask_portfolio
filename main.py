# import "packages" from flask
from flask import Flask, render_template
from blueprint import blueprint
import requests
import json


# create a Flask instance
app = Flask(__name__)
app.register_blueprint(blueprint)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/FunkoPops/')
def funko_pop():
    return render_template("funko_pop.html")


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


@app.route('/darkmode/')
def darkmode():
    return render_template("darkmode.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)


