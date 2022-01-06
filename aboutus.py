# import "packages" from flask
from flask import Flask, render_template, Blueprint
import requests
import json
import random

from __init__ import app

aboutus = Blueprint('aboutus', __name__)

@app.route('/evan/')
def evan():
    return render_template("about_us/evan.html")

@app.route('/leah/')
def leah():
    return render_template("about_us/leah.html")

@app.route('/simon/')
def simon():
    return render_template("about_us/simon.html")

@app.route('/vunsh/')
def vunsh():
    return render_template("about_us/vunsh.html")

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
    url2 = "https://geek-jokes.p.rapidapi.com/api"

    querystring2 = {"format":"json"}

    headers2 = {
        'x-rapidapi-host': "geek-jokes.p.rapidapi.com",
        'x-rapidapi-key': "6279ac9b7amsh7dc015c7d7746fbp1f4d65jsn125b0c500438"
    }

    response2 = requests.request("GET", url2, headers=headers2, params=querystring2)

    output2 = json.loads(response2.text)
    print(output2)
    return render_template("about_us/sanjay.html",data=output,joke=output2)