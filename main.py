# import "packages" from flask
from flask import Flask, render_template
import requests
import json
# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/LucasAboutMe/')
def LucasAboutMe ():
    return render_template("LucasAboutMe.html")

@app.route('/IanAboutMe/')
def IanAboutMe ():
    return render_template("IanAboutMe.html")

@app.route('/KianAboutMe/')
def KianAboutMe ():
    return render_template("KianAboutMe.html")

@app.route('/GavinAboutMe/')
def GavinAboutMe ():
    return render_template("GavinAboutMe.html")


@app.route('/pokemoncards/')
def pokemon_cards():
    url = "https://pokemon-tcg-card-prices.p.rapidapi.com/card/c4cbb4b6-ceba-4b14-8e28-ad2b590ccd59"

    headers = {
        'x-rapidapi-host': "pokemon-tcg-card-prices.p.rapidapi.com",
        'x-rapidapi-key': "7815f70232mshea0c87cc336b4aap13f459jsn464272722115"
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    return render_template("pokemon_cards.html", pokemoncard=data)


@app.route('/sportscards/')
def sports_cards():
    return render_template("sports_cards.html")



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
