from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import requests
import random

from model_jokes import *

app_api = Blueprint('api', __name__,
                   url_prefix='/api/jokes')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api)

class JokesAPI:
    # class for create/post
    class _Create(Resource):
        def post(self, joke):
            pass
            
    # class for read/get
    class _Read(Resource):
        def get(self):
            return jsonify(getJokes())

    # class for delete
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getJoke(id))

    # class for read/get
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomJoke())

    # class for update/put
    class _UpdateLike(Resource):
        def put(self, id):
            addJokeHaHa(id)
            return jsonify(getJoke(id))

    class _UpdateJeer(Resource):
        def put(self, id):
            addJokeBooHoo(id)
            return jsonify(getJoke(id))

    # building RESTapi resource
    # building RESTapi resource
    api.add_resource(_Create, '/create/<string:joke>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_UpdateLike, '/like/<int:id>/')
    api.add_resource(_UpdateJeer, '/jeer/<int:id>/')
    
if __name__ == "__main__": 
    url = 'http://127.0.0.1:5000/api/jokes/' # run from project to enable
    responses = []  # responses list
    
    # responses.append(requests.get(url)) # read all, verbose so commented out
    responses.append(requests.get(url+"random")) # read a random joke
    
    # update likes/dislikes test sequence
    num = str(random.randint(0, countJokes()-1)) # test a random record
    responses.append(
        requests.get(url+num)  # read joke by id
        ) 
    responses.append(
        requests.put(url+"like/"+num) # add to like count
        ) 
    responses.append(
        requests.put(url+"jeer/"+num) # add to jeer count
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")