# import "packages" from flask
from flask import Flask, render_template, request
from crud import app_crud
from __init__ import app
from flask import Blueprint
import requests

from blueprints.connor import bconnor
from blueprints.pranav import bpranav
from blueprints.colin import bcolin
from blueprints.chase import bchase
from blueprints.tanay import btanay
# create a Flask instance
app.register_blueprint(app_crud)
app.register_blueprint(bconnor, url_prefix="/")
app.register_blueprint(bpranav, url_prefix="/")
app.register_blueprint(bcolin, url_prefix="/")
app.register_blueprint(bchase, url_prefix="/")
app.register_blueprint(btanay, url_prefix="/")


@app.route('/')
def index():
    return render_template("index.html")




# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True,port=8000)
