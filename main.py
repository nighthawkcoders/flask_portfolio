from flask import Flask, render_template
from blueprint import blueprint
import requests
import json

app = Flask(__name__)

app.register_blueprint(blueprint)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/F1Schedule/')
def F1Schedule():
    return render_template("F1Schedule.html")


@app.route('/FPCStarWars/')
def FPCStarWars():
    return render_template("FPCStarWars.html")


@app.route('/FPCToyStory/')
def FPCToyStory():
    return render_template("FPCToyStory.html")


@app.route('/FPCPokemon/')
def FPCPokemon():
    return render_template("FPCPokemon.html")


@app.route('/CollectablesGame/')
def CollectablesGame():
    return render_template("CollectablesGame.html")


@app.route('/Pokedex/')
def Pokedex():
    return render_template("Pokedex.html")


@app.route('/PokemonBattle/')
def PokemonBattle():
    return render_template("PokemonBattle.html")


@app.route('/Random/')
def Random():
    return render_template("Random.html")


@app.route('/FunkoPops/')
def funko_pop():
    return render_template("funko_pop.html")


@app.route('/pokemoncards/')
def pokemon_cards():
    url = "https://pokemon-tcg-card-prices.p.rapidapi.com/card"

    querystring = {"setId": "33ee55f4-30d0-4900-850f-36a351fb9719", "set": "vivid-voltage",
                   "series": "sword-and-shield"}

    headers = {
        'x-rapidapi-host': "pokemon-tcg-card-prices.p.rapidapi.com",
        'x-rapidapi-key': "7815f70232mshea0c87cc336b4aap13f459jsn464272722115"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    return render_template("pokemon_cards.html", pokemoncard=data)


@app.route('/fortnite/')
def sports_cards():
    return render_template("fortnite.html")


@app.route('/funkopops/')
def funko_pops():
    return render_template("funko_pops.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True, port=8000)
