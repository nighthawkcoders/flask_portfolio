# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/evan/')
def evan():
    return render_template("evan.html")

@app.route('/leah/')
def leah():
    return render_template("leah.html")

@app.route("/sanjay/")
def sanjay():
    return render_template("sanjay.html")
# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
