# import "packages" from flask
from flask import Flask, render_template,request
import os
import requests

# create a Flask instance
app = Flask(__name__)


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

@app.route('/jason/', methods=['GET', 'POST'])
def jason():
    return render_template("jason.html")


@app.route('/adi/')
def adi():
    return render_template("adi.html")

@app.route('/brian/')
def brian():
    return render_template("brian.html")

@app.route('/rohan', methods=['GET', 'POST'])
def rohan():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("rohan.html", name1=name)
    return render_template("rohan.html", name1="homie")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
