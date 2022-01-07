from flask import Blueprint, render_template
import requests

bcolin = Blueprint("bcolin", __name__, static_folder="static", template_folder="templates")

@bcolin.route('/colin/')
def colin():
    url = "https://free-nba.p.rapidapi.com/players"
    return render_template('colin.html', data=data)

querystring = {"page":"0","per_page":"25"}

headers = {
    'x-rapidapi-host': "free-nba.p.rapidapi.com",
    'x-rapidapi-key': "c9627c0b20msh49d43de4e2620d8p16c0f2jsn67c02d827b55"
}

response = requests.request("GET", url = "https://free-nba.p.rapidapi.com/players", headers=headers, params=querystring)
data = response.json()['data']

print(data)

@bcolin.route('/imageCarousel/')
def imageCarousel():
    return render_template('PBL Pages/imageCarousel.html')

