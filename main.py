# import "packages" from flask

from flask import Flask, render_template, request
import requests

# create a Flask instance
app = Flask(__name__)


from crud3.app_crud import app_crud

#from gigiChat import app_gigiChat
#app.register_blueprint(app_gigiChat)

# create a Flask instance

app.register_blueprint(app_crud)


# connects default URL to render index.html
@app.route('/')
def home():
    return render_template("api/unUsed/home.html")

@app.route('/anikaCraft')
def anikaCraft():
    return render_template("crossTeam/anikaCraft.html")

@app.route('/nehaAPI')
def nehaAPI():
    return render_template("crossTeam/nehaAPI.html")

@app.route('/gigiTitle')
def gigiTitle():
    return render_template("crossTeam/gigiTitle.html")

@app.route('/gigiChat')
def gigiChat():
    return render_template("crossTeam/gigiChat.html")

@app.route('/gigiSnake')
def gigiSnake():
    return render_template("crossTeam/gigiSnake.html")


@app.route('/dark')
def dark():
    return render_template("keyFeatures/dark.html")


@app.route('/study')
def study():
    return render_template("keyFeatures/study.html")


@app.route('/stress')
def stress():
    return render_template("keyFeatures/stress.html")


@app.route('/volunteer')
def volunteer():
    return render_template("keyFeatures/volunteer.html")

@app.route('/eduvidDina')
def eduvidDina():
    return render_template("crossTeam/tinahtmlFolder/eduvidDina.html")


@app.route('/crud/search')
def search():
    return render_template("search.html")


@app.route('/crud')
def crud():
    return render_template("crud.html")

@app.route('/goalsCl')
def goalsCl():
    return render_template("crossTeam/tinahtmlFolder/imbedHtml/goalsCl.html")

@app.route('/organIm')
def organIm():
    return render_template("crossTeam/tinahtmlFolder/imbedHtml/organIm.html")


@app.route('/loveO')
def loveO():
    return render_template("crossTeam/tinahtmlFolder/imbedHtml/loveO.html")

@app.route('/fibonacci')
def fibonacci():
    return render_template("api/Used/fibonacci.html")


@app.route('/sonakshi', methods=['GET', 'POST'])
def sonakshi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("team/sonakshi.html", name=name)
    # starting and empty input default
    return render_template("team/sonakshi.html", name="World")


@app.route('/forum', methods=['GET', 'POST'])
def forum():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("keyFeatures/forum.html", name=name)
    # starting and empty input default
    return render_template("keyFeatures/forum.html", name="Advice Here")


@app.route('/journal', methods=['GET', 'POST'])
def journal():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("keyFeatures/journal.html", name=name)
    # starting and empty input default
    return render_template("keyFeatures/journal.html", name="Feel Free to Write")


@app.route('/shreya', methods=['GET', 'POST'])
def shreya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("team/shreya.html", name=name)
    # starting and empty input default
    return render_template("team/shreya.html", name="World")


@app.route('/punnu', methods=['GET', 'POST'])
def punnu():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("team/punnu.html", name=name)
    return render_template("team/punnu.html")


@app.route('/khushi', methods=['GET', 'POST'])
def khushi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("team/khushi.html", name=name)
    # starting and empty input default
    return render_template("team/khushi.html", name="World")


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

@app.route('/quote', methods=['GET', 'POST'])
def quote():
    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = {"key": "value"}

    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "motivational-quotes1.p.rapidapi.com",
        'x-rapidapi-key': "69b86a4f86msh0f84d36c298ca22p15693fjsne0d137318725"
    }


@app.route('/trivia', methods=['GET', 'POST'])
def trivia():
    url = "https://numbersapi.p.rapidapi.com/random/trivia"

    querystring = {"min":"1","max":"100","fragment":"true","json":"true"}

    headers = {
        'x-rapidapi-host': "numbersapi.p.rapidapi.com",
        'x-rapidapi-key': "69b86a4f86msh0f84d36c298ca22p15693fjsne0d137318725"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("keyFeatures/trivia.html", numbers=response.json())
    print(response.text)


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

    return render_template("api/unUsed/listmovieapi.html", response=response)



@app.route('/dictionary', methods=['GET', 'POST'])
def dictionary():
    word = "fantastic"
    url = "https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary"
    querystring = {"word": word}
    headers = {
        'x-rapidapi-host': "dictionary-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "69b86a4f86msh0f84d36c298ca22p15693fjsne0d137318725"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("api/unUsed/dictionary.html", word=word, stats=response.json())

@app.route('/punnuapitest', methods=['GET', 'POST'])
def punnuapitest():
    url = "https://api.kuroganehammer.com/api/characters"
    response = requests.request("GET", url)
    text = response.json()
    return render_template("team/punnuapitest.html", text=text)

@app.route('/stressCrafts')
def stressCrafts():
    return render_template("stressCrafts.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True, port="5001")
