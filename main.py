# import "packages" from flask

from flask import Flask, render_template, request
import requests
import http.client
# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/sonakshi', methods=['GET', 'POST'])
def sonakshi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("sonakshi.html", name=name)
    # starting and empty input default
    return render_template("sonakshi.html", name="World")

@app.route('/shreya', methods=['GET', 'POST'])
def shreya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("shreya.html", name=name)
    # starting and empty input default
    return render_template("shreya.html", name="World")

@app.route('/genius', methods=['GET', 'POST'])
def genius():
    url = "https://genius.p.rapidapi.com/songs/442856"

    headers = {
        'x-rapidapi-host': 'genius.p.rapidapi.com',
        'x-rapidapi-key': '4c61a908e2mshb55cf4906131117p1da9ffjsnde3b82957ef9'
    }

    response = requests.request("GET", url, headers=headers)

    return render_template("genius.html", stats=response.json())

@app.route('/linda', methods=['GET', 'POST'])
def linda():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("linda.html", name=name)
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
    querystring = {"q": "San Diego"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "8d571b2f72msh44f8fd48e083624p19cce1jsnfb1e373c1716"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return render_template("newapi.html", stats=response.json())

@app.route('/listmovie/', methods=['GET', 'POST'])
def listmovie():
    url = "https://watchmode.p.rapidapi.com/list-titles/"

    querystring = {"types": "movie,tv_series", "regions": "US", "source_types": "sub,free", "source_ids": "23,206",
                   "page": "1", "limit": "250", "genres": "4,9"}  # assigns values to specified parameters(keys)

    headers = {
        'x-rapidapi-host': "watchmode.p.rapidapi.com",
        'x-rapidapi-key': "f4480562c7mshcfebe0975d4fd48p16ab77jsnae6575329780"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json().get("titles")

    return render_template("listmovie.html", response=response)

@app.route ('/dictionary', methods=['GET', 'POST'])
def dictionary():

    word = "fantastic"
    url = "https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary"
    querystring = {"word":word}
    headers = {
        'x-rapidapi-host': "dictionary-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "69b86a4f86msh0f84d36c298ca22p15693fjsne0d137318725"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("dictionary.html", word=word, stats=response.json())

@app.route('/punnuapitest', methods=['GET', 'POST'])
def punnuapitest():
    url = "https://api.kuroganehammer.com/api/characters"
    response = requests.request("GET", url)
    text = response.json()
    return render_template("/punnuapitest.html", text=text)



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
