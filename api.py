from flask import Blueprint, jsonify
from model_jokes import joke_random, jokes

app_api = Blueprint('api', __name__,
                   url_prefix='/api')

@app_api.route('/joke')
def api_joke():
    return jsonify(joke_random())

@app_api.route('/jokes')
def api_jokes():
    return jsonify(jokes())