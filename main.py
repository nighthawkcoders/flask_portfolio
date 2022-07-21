# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
from __init__ import app  # import initialization from "this" project
from api import app_api # import api definition from "this" project
app.register_blueprint(app_api) # register api routes

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

@app.route('/stub/')
def stub():
    return render_template("stub.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
