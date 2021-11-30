# import "packages" from flask
from flask import Flask, render_template

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


@app.route('/samaya/')
def samaya():
    return render_template("samaya.html")


@app.route('/alice/')
def alice():
    return render_template("alice.html")


@app.route('/pranavi/')
def pranavi():
    return render_template("pranavi.html")


@app.route('/saathvika/')
def saathvika():
    return render_template("saathvika.html")


@app.route('/linda/')
def linda():
    return render_template("linda.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
