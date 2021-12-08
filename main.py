# import "packages" from flask
from flask import Flask, render_template, request
import requests

from nathan.nathan import nathan_bp
# create a Flask instance
app = Flask(__name__)


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

app.register_blueprint(nathan_bp)

app.run(host="127.0.0.1", port=5000)
# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
