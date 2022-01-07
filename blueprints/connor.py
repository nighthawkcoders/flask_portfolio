from flask import Blueprint, render_template
import requests
from algorithms.petinfo import pinfo
from pathlib import Path

bconnor = Blueprint("bconnor", __name__, static_folder="static", template_folder="templates")

@bconnor.route('/connor/')
def connor():
    return render_template('connor.html')
    url = "https://genius.p.rapidapi.com/artists/16775/songs"

    headers = {
        'x-rapidapi-host': "genius.p.rapidapi.com",
        'x-rapidapi-key': "e96b80de18msh080ccecb09304e3p1f9084jsn90d405c70ce3"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()['response']['songs']

    print(data)
    return render_template('connor.html', data=data)


@bconnor.route('/PetInfo/')
def PetInfo():
    path = Path(bconnor.root_path) / "testconnorimages"
    return render_template('PetInfo.html', pimage=pinfo(path))