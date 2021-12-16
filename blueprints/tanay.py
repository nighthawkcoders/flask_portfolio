from flask import Blueprint, render_template
import requests

btanay = Blueprint("btanay", __name__, static_folder="static", template_folder="templates")

@btanay.route('/tanay/', methods=['GET', 'POST'])
def tanay():
    url = "https://sportscore1.p.rapidapi.com/sports/1/teams"
    headers = {
        'x-rapidapi-host': "sportscore1.p.rapidapi.com",
        'x-rapidapi-key': "39c4bf8c2emsh30b02ab6dc01dd9p13f427jsn690a650cf2ec"
    }
    # return render_template("tanay.html")

    response = requests.request("GET", url, headers=headers)
    return render_template("tanay.html", stats=response.json())