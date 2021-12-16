from flask import Blueprint, render_template
import requests

bpranav = Blueprint("bpranav", __name__, static_folder="static", template_folder="templates")

@bpranav.route('/pranav/')
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

@bpranav.route('/dogs/')
def dogs():
    return render_template('dogs.html')
