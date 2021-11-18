# import "packages" from flask
from flask import Flask, render_template
from pathlib import Path

# create a Flask instance
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/connor/')
def connor():
    return render_template('connor.html')

@app.route('/tanay/')
def tanay():
    return render_template('tanay.html')

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
