from flask import Flask, Blueprint, render_template, request
import requests

about_pg = Blueprint('about', __name__,
                   url_prefix='/about',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/about')



darkmode="darkmode"
# connects default URL to render index.html

@about_pg.route('/jason/')
def jason():
    url = "https://video-game-news.p.rapidapi.com/star_wars"

    headers = {
        'x-rapidapi-host': "video-game-news.p.rapidapi.com",
        'x-rapidapi-key': "9c2bef1841msh474f0e89d12625ap15b46cjsn29537babe185"
    }

    response = requests.request("GET", url, headers=headers)

    final=response.text
    return render_template("aboutpages/jason.html", darkmode=darkmode)


@about_pg.route('/adi', methods={'GET', 'POST'})
def adi():
    url = "https://sportscore1.p.rapidapi.com/sports/1/teams"
    headers = {
        'x-rapidapi-host': "sportscore1.p.rapidapi.com",
        'x-rapidapi-key': "39c4bf8c2emsh30b02ab6dc01dd9p13f427jsn690a650cf2ec"
    }

    response = requests.request("GET", url, headers=headers)
    return render_template("aboutpages/adi.html", stats=response.json(), darkmode=darkmode)

@about_pg.route('/brian')
def brian():
    # url = "https://tennis-live-data.p.rapidapi.com/tournaments/ATP/2020"
    # headers = {
    #     'x-rapidapi-host': "tennis-live-data.p.rapidapi.com",
    #     'x-rapidapi-key': "3d43659d98msh26d5e705bc7d8b6p1d6431jsnba44357aaf20"
    # }
    # response = requests.request("GET", url, headers=headers)
    # results = json.loads(response.content.decode("utf-8"))['results']
    return render_template("aboutpages/brian.html", darkmode=darkmode)#, res=results)

@about_pg.route('/divya')
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
    return render_template("aboutpages/divya.html", quotes=quotes, darkmode=darkmode)

@about_pg.route('/rohan', methods=['GET', 'POST'])
def rohan():
    url = "https://free-nba.p.rapidapi.com/players"

    headers = {
        'x-rapidapi-host': "free-nba.p.rapidapi.com",
        'x-rapidapi-key': "35a01f5f74msh20628303ae6dbefp168484jsn83f86e2f8568"
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return render_template("aboutpages/rohan.html", data=data, darkmode=darkmode)
