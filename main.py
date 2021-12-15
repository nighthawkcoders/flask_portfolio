# import "packages" from flask

from flask import render_template, request
from __init__ import app
import requests
import json

from crud.app_crud import app_crud
app.register_blueprint(app_crud)


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

@app.route('/jason/')
def jason():
    url = "https://video-game-news.p.rapidapi.com/star_wars"

    headers = {
        'x-rapidapi-host': "video-game-news.p.rapidapi.com",
        'x-rapidapi-key': "9c2bef1841msh474f0e89d12625ap15b46cjsn29537babe185"
    }

    response = requests.request("GET", url, headers=headers)

    final=response.text
    return render_template("jason.html")




@app.route('/adi/', methods={'GET', 'POST'})
def adi():
    url = "https://sportscore1.p.rapidapi.com/sports/1/teams"
    headers = {
        'x-rapidapi-host': "sportscore1.p.rapidapi.com",
        'x-rapidapi-key': "39c4bf8c2emsh30b02ab6dc01dd9p13f427jsn690a650cf2ec"
    }
    # return render_template("AboutDylan.html")

    response = requests.request("GET", url, headers=headers)
    return render_template("adi.html", stats=response.json())

@app.route('/brian/')
def brian():
    url = "https://tennis-live-data.p.rapidapi.com/tournaments/ATP/2020"
    headers = {
        'x-rapidapi-host': "tennis-live-data.p.rapidapi.com",
        'x-rapidapi-key': "3d43659d98msh26d5e705bc7d8b6p1d6431jsnba44357aaf20"
    }
    response = requests.request("GET", url, headers=headers)
    results = json.loads(response.content.decode("utf-8"))['results']
    return render_template("brian.html", res=results)

@app.route('/divya/')
def divya():
    url = "https://famous-quotes4.p.rapidapi.com/random"
    querystring = {"category":"all","count":"2"}
    headers = {
        'x-rapidapi-host': "famous-quotes4.p.rapidapi.com",
        'x-rapidapi-key': "80afb5b6afmsh552d92e769ba3a5p1bfac9jsnfb6c407dd20f"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    quotes = []
    for result in response:
        quotes.append(result['text'] + " by author: " + result['author'])
    return render_template("divya.html", quotes=quotes)

@app.route('/rohan', methods=['GET', 'POST'])
def rohan():
    url = "https://free-nba.p.rapidapi.com/players"

    headers = {
       'x-rapidapi-host': "free-nba.p.rapidapi.com",
        'x-rapidapi-key': "35a01f5f74msh20628303ae6dbefp168484jsn83f86e2f8568"
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return render_template("rohan.html", data=data)

@app.route('/photogallery', methods=['GET', 'POST'])
def photogallery():
    if request.form:
        input = request.form.get("input")
        if len(input) != 0:
            return render_template("photogallery.html", input1=input)
    return render_template("photogallery.html", input1="")

@app.route('/weather/')
def weather():
    return render_template("weather.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True,port=8081)
