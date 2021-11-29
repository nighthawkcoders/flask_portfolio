# import "packages" from flask
from flask import Flask, render_template,request
import os
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

@app.route('/jason/', methods=['GET', 'POST'])
def jason():
    return render_template("jason.html")


@app.route('/adi/')
def adi():
    return render_template("adi.html")

@app.route('/brian/')
def brian():
    url = "https://tennis-live-data.p.rapidapi.com/matches-by-date/2020-09-06"

    headers = {
        'x-rapidapi-host': "tennis-live-data.p.rapidapi.com",
        'x-rapidapi-key': "3d43659d98msh26d5e705bc7d8b6p1d6431jsnba44357aaf20"
    }

    response = requests.request("GET", url, headers=headers)
    results = json.loads(response.content.decode("utf-8"))['results']
    tournaments = []
    for result in results:
        # result['tournament']
        tournaments.append(result['tournament'])
    # tournament = json.loads(response.content.decode("utf-8"))['results'][0]['tournament']
    return render_template("brian.html", tournaments=tournaments)

@app.route('/divya/')
def divya():
    return render_template("divya.html")

@app.route('/rohan', methods=['GET', 'POST'])
def rohan():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("rohan.html", name1=name)
    return render_template("rohan.html", name1="homie")

# Genius Lyrics api
url = "https://genius.p.rapidapi.com/artists/16775/songs"

headers = {
    'x-rapidapi-host': "genius.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True,port=8000)
