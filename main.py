# import "packages" from flask
from flask import Flask, render_template
import requests
import json
import random
# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/evan/')
def evan():
    return render_template("evan.html")

@app.route('/leah/')
def leah():
    return render_template("leah.html")

@app.route("/sanjay/")
def sanjay():
    options = ["soccer_efl_champ","soccer_epl","soccer_england_efl_cup","soccer_england_league1","soccer_england_league2"]
    selection = options[random.randint(0,len(options)-1)]
    url = "https://odds.p.rapidapi.com/v1/odds"

    querystring = {"sport":"soccer_epl","region":"uk","mkt":"h2h","dateFormat":"iso","oddsFormat":"decimal"}

    headers = {
        'x-rapidapi-host': "odds.p.rapidapi.com",
        'x-rapidapi-key': "6279ac9b7amsh7dc015c7d7746fbp1f4d65jsn125b0c500438"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    output =json.loads(response.text)
    return render_template("sanjay.html",data=output)
# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
