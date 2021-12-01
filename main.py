# import "packages" from flask
from pathlib import Path

from flask import Flask, render_template, request
from algorithms.image import rotatehack, sonakshi_image_data, kashish_image_data, saumya_image_data
import requests

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def home():
    return render_template("home.html")


# connects /kangaroos path to render home.html






@app.route('/stub/')
def stub():
    return render_template("stub.html")





@app.route('/sonakshi', methods=['GET', 'POST'])
def sonakshi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("sonakshi.html", name=name)
    # starting and empty input default
    return render_template("sonakshi.html", name="World")
# starting and empty input default

@app.route('/shreya', methods=['GET', 'POST'])
def shreya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("shreya.html", name=name)
    # starting and empty input default
    return render_template("shreya.html", name="World")
# starting and empty input default


@app.route('/genius', methods=['GET', 'POST'])
def genius():

    url = "https://genius.p.rapidapi.com/songs/442856"

    headers = {
        'x-rapidapi-host': 'genius.p.rapidapi.com',
        'x-rapidapi-key': '4c61a908e2mshb55cf4906131117p1da9ffjsnde3b82957ef9'
    }

    response = requests.request("GET", url, headers=headers)

    return render_template("genius.html", stats=response.json())


@app.route('/linda')
def linda():
    return render_template("linda.html")

@app.route('/khushi', methods=['GET', 'POST'])
def khushi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("khushi.html", name=name)
    # starting and empty input default
    return render_template("khushi.html", name="World")

















@app.route('/newapi', methods=['GET', 'POST'])
def newapi():

    url = "https://community-open-weather-map.p.rapidapi.com/climate/month"
    querystring = {"q":"San Diego"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "8d571b2f72msh44f8fd48e083624p19cce1jsnfb1e373c1716"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return render_template("newapi.html", stats=response.json())

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
