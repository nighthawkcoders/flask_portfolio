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
@app.route('/asia/')
def asia():
    return render_template("asia.html")

@app.route('/africa/')
def africa():
    return render_template("africa.html")


@app.route('/northamerica/')
def northamerica():
    return render_template("northamerica.html")

@app.route('/southamerica/')
def southamerica():
    return render_template("southamerica.html")

@app.route('/antarctica/')
def antarctica():
    return render_template("antarctica.html")

@app.route('/europe/')
def europe():
    return render_template("europe.html")

@app.route('/australia/')
def australia():
    return render_template("australia.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route("/binary", methods=['GET','POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary.html", bits=int(bits))
        # starting and empty input default
    return render_template("binary.html", bits=8)



@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route("/addition", methods=['GET','POST'])
def addition():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("addition.html", bits=int(bits))
        # starting and empty input default
    return render_template("addition.html", bits=8)

@app.route("/signed", methods=['GET','POST'])
def signed():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("signed.html", bits=int(bits))
        # starting and empty input default
    return render_template("signed.html", bits=8)

@app.route('/sonakshi', methods=['GET', 'POST'])
def sonakshi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("sonakshi.html", name=name)
    # starting and empty input default
    return render_template("sonakshi.html", name="World")

@app.route('/saumya', methods=['GET', 'POST'])
def saumya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("saumya.html", name=name)
    # starting and empty input default
    return render_template("saumya.html", name="World")

@app.route('/kashish', methods=['GET', 'POST'])
def kashish():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("kashish.html", name=name)
    # starting and empty input default
    return render_template("kashish.html", name="World")



@app.route('/insights/')
def insights():
    return render_template("insights.html")

@app.route('/greet/')
def greet():
    return render_template("greet.html")

@app.route('/color/', methods=['GET', 'POST'])
def color():
    BITS=8
    imgBulbOn = "static/assets/openbook.jpg"
    if request.form:
        BITS = int(request.form.get("BITS"))
        imgBulbOn = request.form['lightOn']
    return render_template("color.html", imgBulbOn=imgBulbOn, BITS=BITS)

@app.route('/logic gates/')
def logicgates():
    return render_template("logicgates.html")

@app.route('/sevenwonders/')
def sevenwonders():
    return render_template("sevenwonders.html")



@app.route('/covid', methods=['GET', 'POST'])
def covid():
        url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
        headers = {
            'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
            'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        """
        # uncomment this code to test from terminal
        world = response.json().get('world_total')
        countries = response.json().get('countries_stat')
        print(world['total_cases'])
        for country in countries:
            print(country["country_name"])
        """
        # return response.text
        return render_template("covid.html", stats=response.json())



@app.route('/flightapi', methods=['GET', 'POST'])
def flightapi(place: str = "china"):

    # import requests

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/US/USD/en-US/"

    querystring = {"query": "san diego"}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "8d571b2f72msh44f8fd48e083624p19cce1jsnfb1e373c1716"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # return(response.text)
    return render_template("flightapi.html", stats=response.json())



@app.route('/flightdata', methods=['GET', 'POST'])
def flightdata():

# import requests

    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

    querystring = {"lon":"117.1611","lat":"32.7157"}

    headers = {
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
        'x-rapidapi-key': "8d571b2f72msh44f8fd48e083624p19cce1jsnfb1e373c1716"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return (response.text)

    return render_template("flightdata.html", stats=response.json())


@app.route('/accommodationsapi', methods=['GET', 'POST'])
def accommodationsapi():

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/countries/en-US"

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "8d571b2f72msh44f8fd48e083624p19cce1jsnfb1e373c1716"
    }

    response = requests.request("GET", url, headers=headers)

    # return(response.text)
    return render_template("listofcountriesapi.html", stats=response.json())

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
