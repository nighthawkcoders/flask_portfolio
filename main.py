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


@app.route('/samaya/')
def samaya():
    return render_template("samaya.html")


@app.route('/alice/')
def alice():
    url = "https://brianiswu-cat-facts-v1.p.rapidapi.com/facts"

    headers = {
        'x-rapidapi-host': "brianiswu-cat-facts-v1.p.rapidapi.com",
        'x-rapidapi-key': "f877084053msh82cfa972b631ab7p1c4893jsn442e2f514bb0"
    }

    response = requests.request("GET", url, headers=headers)
    # how long is the response.json, 0-4, random, 0-8
    output = response.json()     #5 items long
    return render_template("alice.html", output=output)


@app.route('/pranavi/')
def pranavi():
    return render_template("pranavi.html")


@app.route('/saathvika/')
def saathvika():
    return render_template("saathvika.html")


@app.route('/linda/')
def linda():
    return render_template("linda.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
