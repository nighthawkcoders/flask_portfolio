# import "packages" from flask
from flask import Flask, render_template
from flask import request
from __init__ import app
from crud.app_crud import app_crud
import requests

# create a Flask instance
# app = Flask(__name__)
app.register_blueprint(app_crud)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/aboutnathan')
def aboutnathan():
    return render_template("aboutnathan.html")

@app.route('/aboutreem')
def aboutreem():
    return render_template("aboutreem.html")


@app.route('/aboutjacob')
def aboutjacob():
    return render_template("aboutjacob.html")


@app.route('/aboutjames')
def aboutjames():
    return render_template("aboutjames.html")


@app.route('/aboutdaniel')
def aboutdaniel():
    return render_template("aboutdaniel.html")

@app.route('/mainabout/')
def mainabout():
    return render_template("mainabout.html")

@app.route('/worldclock/')
def worldclock():
    return render_template("worldclock.html")

@app.route('/feedback/', methods=['GET', 'POST'])
def feedback():
    if request.form:
        input = request.form.get("feed1")
        name = request.form.get("feed2")
        if len(input) != 0:  # input field has content
            return render_template("layouts/feedback.html", input=input, name=name)
    return render_template("layouts/feedback.html")

@app.route('/translator/', methods=['GET', 'POST'])
def translator():
    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"
    pairs = ["en|es", "en|it", "en|zh", "en|de", "en|he"]
    text = "Translated text will show here"
    original = text
    master_list = []
    if request.form:
        text = request.form.get("tester2")
        original = text
    for item in pairs:
        querystring = {"langpair":item,"q":text,"mt":"1","onlyprivate":"0","de":"a@b.c"}

        headers = {
            'x-rapidapi-host': "translated-mymemory---translation-memory.p.rapidapi.com",
            'x-rapidapi-key': "00a6319afcmshb59ecb31e0a9dbap1c6de4jsn4b86a9198483"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        dictionary = [response.json().get('responseData')]
        master_list = master_list + dictionary
    return render_template("layouts/translator.html", dictionary=master_list, original=original)

@app.route('/crud')
def crud():
    return render_template("crud.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/weather/', methods=['GET', 'POST'])
def weather():
    countrycode = ['105391811', '105368361', '105359777', '105341704', '105393052', '105392171']
    dictionarymasterlist = []  # this creates an empty list that all the dictionaries go into
    for item in countrycode:  # this is a for loop for all the country codes so that each one gets a response
        url = "https://foreca-weather.p.rapidapi.com/observation/latest/" + item

        querystring = {"lang": "en"}

        headers = {
            'x-rapidapi-host': "foreca-weather.p.rapidapi.com",
            'x-rapidapi-key': "00a6319afcmshb59ecb31e0a9dbap1c6de4jsn4b86a9198483"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        list_of_dictionaries2 = response.json().get('observations')
        dictionarymasterlist = dictionarymasterlist + list_of_dictionaries2
    print('WEATHER INFO')
    print(dictionarymasterlist)
    return render_template("layouts/weather.html", weather=dictionarymasterlist)



# runs the application on the development server
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
