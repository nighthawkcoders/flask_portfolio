from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import json

from model.sqliteDB import *

user_api = Blueprint('user_api', __name__,
                   url_prefix='/api/users')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(user_api)

class UserAPI:        
    # getJokes()
    class _Read(Resource):
        def get(self):
            users = User.query.all()
            json_ready = [user.read() for user in users]
            return jsonify(json_ready)
        
     # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Read, '/')