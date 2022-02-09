# import "packages" from flask
from flask import Flask, render_template
from flask import request
from __init__ import app
import requests, random

from crud.app_crud_api import app_crud_api
app.register_blueprint(app_crud_api)

# create a Flask instance
# app = Flask(__name__)
from crud.app_crud import app_crud
app.register_blueprint(app_crud)

from aboutme import app_aboutme
app.register_blueprint(app_aboutme)

from api import app_api
app.register_blueprint(app_api)

from games import app_games
app.register_blueprint(app_games)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

fivestars_list = []
fourstars_list = []
threestars_list = []
twostars_list = []
onestar_list = []


@app.route('/ratingtest/')
def ratingtest():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(
        fivestars_list) * 5
    if total != 0:
        average = sum / total
    else:
        average = 0
    return render_template("ratingtest.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list,
                           threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list,
                           average=average)


@app.route('/fivestars', methods=['GET', 'POST'])
def fivestars():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(
        fivestars_list) * 5
    if total != 0:
        average = sum / total
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            fivestars_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(
                fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(
                fivestars_list) * 5
            if total != 0:
                average = sum / total
            else:
                average = 0
            return render_template("ratingtest.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list,
                                   threestarsreview=threestars_list, twostarsreview=twostars_list,
                                   onestarreview=onestar_list, average=average)
    return render_template("ratingtest.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list,
                           threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list,
                           average=average)


@app.route('/fourstars', methods=['GET', 'POST'])
def fourstars():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(
        fivestars_list) * 5
    if total != 0:
        average = sum / total
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            fourstars_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(
                fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(
                fivestars_list) * 5
            if total != 0:
                average = sum / total
            else:
                average = 0
            return render_template("ratingtest.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list,
                                   threestarsreview=threestars_list, twostarsreview=twostars_list,
                                   onestarreview=onestar_list, average=average)
    return render_template("ratingtest.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list,
                           threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list,
                           average=average)


@app.route('/threestars', methods=['GET', 'POST'])
def threestars():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(
        fivestars_list) * 5
    if total != 0:
        average = sum / total
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            threestars_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(
                fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(
                fivestars_list) * 5
            if total != 0:
                average = sum / total
            else:
                average = 0
            return render_template("ratingtest.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list,
                                   threestarsreview=threestars_list, twostarsreview=twostars_list,
                                   onestarreview=onestar_list, average=average)
    return render_template("ratingtest.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list,
                           threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list,
                           average=average)


@app.route('/twostars', methods=['GET', 'POST'])
def twostars():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(
        fivestars_list) * 5
    if total != 0:
        average = sum / total
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            twostars_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(
                fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(
                fivestars_list) * 5
            if total != 0:
                average = sum / total
            else:
                average = 0
            return render_template("ratingtest.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list,
                                   threestarsreview=threestars_list, twostarsreview=twostars_list,
                                   onestarreview=onestar_list, average=average)
    return render_template("ratingtest.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list,
                           threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list,
                           average=average)


@app.route('/onestar', methods=['GET', 'POST'])
def onestar():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(
        fivestars_list) * 5
    if total != 0:
        average = sum / total
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            onestar_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(
                fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(
                fivestars_list) * 5
            if total != 0:
                average = sum / total
            else:
                average = 0
            return render_template("ratingtest.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list,
                                   threestarsreview=threestars_list, twostarsreview=twostars_list,
                                   onestarreview=onestar_list, average=average)
    return render_template("ratingtest.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list,
                           threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list,
                           average=average)


@app.route('/feedback/', methods=['GET', 'POST'])
def feedback():
    if request.form:
        input = request.form.get("feed1")
        name = request.form.get("feed2")
        if len(input) != 0:  # input field has content
            return render_template("layouts/feedback.html", input=input, name=name)
    return render_template("layouts/feedback.html")

@app.route('/crud')
def crud():
    return render_template("crud.html")

@app.route('/crud_api')
def crud_async():
    return render_template("crud_async.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/countries')
def countries():
    return render_template("countries.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")

@app.route('/infopage')
def infopage():
    return render_template("infopage.html")

@app.route('/currency', methods=['GET', 'POST'])
def currency():
    return render_template("layouts/currency.html")

@app.route('/world_instruments', methods=['GET', 'POST'])
def world_instruments():
    return render_template("layouts/world_instruments.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)

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
        querystring = {"langpair":item,"q":text , "mt":"1","onlyprivate":"0","de":"a@b.c"}

        headers = {
            'x-rapidapi-host': "translated-mymemory---translation-memory.p.rapidapi.com",
            'x-rapidapi-key': "00a6319afcmshb59ecb31e0a9dbap1c6de4jsn4b86a9198483"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        dictionary = [response.json().get('responseData')]
        master_list = master_list + dictionary
    return render_template("layouts/translator.html", dictionary=master_list, original=original)

@app.route('/population', methods=['GET', 'POST'])
def population():
    CountryList = [
        'China',
        'India',
        'United States',
        'Indonesia',
        'Pakistan',
        'Brazil',
        'Nigeria',
        'Bangladesh',
        'Russia',
        'Mexico',
        'Japan',
        'Ethiopia',
        'Philippines',
        'Egypt',
        'Vietnam',
        'DR Congo',
        'Turkey',
        'Iran',
        'Germany',
        'Thailand',
        'United Kingdom',
        'France',
        'Italy',
        'Tanzania',
        'South Africa'
    ]  # this creates an empty list of all the country names
    top10 = [
        'China',
        'India',
        'United States',
        'Indonesia',
        'Pakistan',
        'Brazil',
        'Nigeria',
        'Bangladesh',
        'Russia',
        'Mexico']

    headers = {
        'x-rapidapi-host': 'world-population.p.rapidapi.com',
        'x-rapidapi-key': 'f4480562c7mshcfebe0975d4fd48p16ab77jsnae6575329780'
    }

    # get all the data for each country
    dictionarymasterlist = []  # this creates an empty list that all the dictionaries go into
    url = "https://world-population.p.rapidapi.com/population"

    CountryList = top10
    for item in CountryList:
        querystring = {"country_name": item}
        response = requests.request("GET", url, headers=headers, params=querystring)

        list_of_dictionaries2 = response.json().get('body')
        dictionarymasterlist = dictionarymasterlist + [list_of_dictionaries2]


    return render_template("layouts/population.html", people=dictionarymasterlist)

@app.route('/environmental/', methods=['GET', 'POST'])
def environmental():
    headers = {
        'x-rapidapi-host': 'environment-news-live.p.rapidapi.com',
        'x-rapidapi-key': 'f4480562c7mshcfebe0975d4fd48p16ab77jsnae6575329780'
    }

    # get list of newspapers
    querystring = {}
    urlNewsList = "https://environment-news-live.p.rapidapi.com/newspapers"
    response = requests.request("GET", urlNewsList, headers=headers, params=querystring)

    list_of_papers = []
    list_of_papers = response.json()  # get('body').get('countries')

    # get all the articles of each source
    dictionarymasterlist = []  # this creates an empty list that all the dictionaries go into

    for item in list_of_papers:
        print(item)
        PaperName = item.get('newspaperID')
        if (PaperName != 'latimes' and PaperName != 'telegraph') : continue

        urlPaper= 'https://environment-news-live.p.rapidapi.com/news/%s' % PaperName
        querystring = {"newspaperID": PaperName}
        response = requests.request("GET", urlPaper, headers=headers, params=querystring)

        list_of_articles = response.json()  # get('body').get('countries')
        dictionarymasterlist = dictionarymasterlist + list_of_articles

    print(dictionarymasterlist)
    return render_template("layouts/environmental.html", news=dictionarymasterlist)











