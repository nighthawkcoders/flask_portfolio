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

@app.route('/currency', methods=['GET', 'POST'])
def currency():
    return render_template("layouts/currency.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
