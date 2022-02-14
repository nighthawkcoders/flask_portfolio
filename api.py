from flask import Blueprint, render_template, app, request
import requests

app_api = Blueprint('api', __name__)

@app_api.route('/worldclock/')
def worldclock():
    return render_template("worldclock.html")

@app_api.route('/population', methods=['GET', 'POST'])
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

@app_api.route('/environmental/', methods=['GET', 'POST'])
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

@app_api.route('/translator/', methods=['GET', 'POST'])
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

@app_api.route('/weather/', methods=['GET', 'POST'])
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