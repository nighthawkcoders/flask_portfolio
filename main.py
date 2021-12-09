# import "packages" from flask
from flask import Flask, render_template
from pathlib import Path
from ChaseAPI import game
# create a Flask instance
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/connor/')
def connor():
    return render_template('connor.html')

@app.route('/Chase/')
def chase():
    return render_template('Chase.html', fgame=game())

@app.route('/tanay/')
def tanay():
    return render_template('tanay.html')

@app.route('/colin/')
def colin():
    return render_template('colin.html')

@app.route('/pranav/')
def pranav():
    return render_template('pranav.html')



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
