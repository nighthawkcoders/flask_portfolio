# import "packages" from flask
from flask import Flask, render_template
import requests
from pathlib import Path

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
    return render_template('Chase.html')

@app.route('/tanay/')
def tanay():
    return render_template('tanay.html')

@app.route('/colin/')
def colin():
    return render_template('colin.html')

@app.route('/pranav/')
def pranav():
    url = "https://free-football-soccer-videos.p.rapidapi.com/"

    headers = {
        'x-rapidapi-host': "free-football-soccer-videos.p.rapidapi.com",
        'x-rapidapi-key': "a52c00a742mshc6c13b49056f1c7p11b54cjsnc5e7c51a6001"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()

    print(response.json())
    return render_template('pranav.html', data=data[-5:])



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
