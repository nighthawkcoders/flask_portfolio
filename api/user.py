import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response, g
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required

from model.users import User

user_api = Blueprint('user_api', __name__,
                   url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(user_api)

class UserAPI:        
    class _ID(Resource):  # Individual identification API operation
        @token_required()
        def get(self):
            ''' Retrieve the current user from the token_required authenication check '''
            current_user = g.current_user
            ''' Return the current user as a json object '''
            return jsonify(current_user.read())
         
    class _CRUD(Resource):  # Users API operation for Create, Read, Update, Delete 
        def post(self): # Create method
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 400
            # validate uid
            uid = body.get('uid')
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 400
            # look for password and dob
            password = body.get('password')
            dob = body.get('dob')

            ''' #1: Key code block, setup USER OBJECT '''
            uo = User(name=name, 
                      uid=uid)
            
            ''' Additional garbage error checking '''
            # set password if provided
            if password is not None:
                uo.set_password(password)
            # convert to date type
            if dob is not None:
                try:
                    uo.dob = datetime.strptime(dob, '%Y-%m-%d').date()
                except:
                    return {'message': f'Date of birth format error {dob}, must be mm-dd-yyyy'}, 400
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            user = uo.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {name}, either a format error or User ID {uid} is duplicate'}, 400

        @token_required()
        def get(self):
            # retrieve the current user from the token_required authenication check  
            current_user = g.current_user
            # current_user extracted from the token using token_required decorator
            users = User.query.all() # extract all users from the database
             
            # prepare a json list of user dictionaries
            json_ready = []  
            for user in users:
                user_data = user.read()
                if current_user.role == 'Admin' or current_user.id == user.id:
                    user_data['access'] = ['rw'] # read-write access control 
                else:
                    user_data['access'] = ['ro'] # read-only access control 
                json_ready.append(user_data)
            
            # return response, a json list of user dictionaries
            return jsonify(json_ready)
        
        @token_required() 
        def put(self):  # Update method
            # retrieve the current user from the token_required authenication check  
            current_user = g.current_user
            
            ''' Read data for json body '''
            body = request.get_json()
           
            ''' Find user '''
            id = body.get('id')
            if id is None:  # if id is not provided
                return {
                    "message": "User ID is required",
                    "data": None,
                    "error": "Bad request"
                }, 400
            ''' Get requested user from the database '''    
            user = User.query.get(id)
            if user is None:    # if user is not found
                return {
                    "message": f"User {id} not found",
                    "data": None,
                    "error": "Not found"
                }, 404
            ''' Check if user is owner or admin ''' 
            if not (current_user.role == 'Admin' or current_user.id == user.id):
                return {
                        "message": "Insufficient permissions, user is not owner or admin.",
                        "data": None,
                        "error": "Unauthorized"
                    }, 403
             
            ''' Update any fields that have data '''
            name = body.get('name')
            if name is not None and name != '':
                user.name = name
                
            uid = body.get('uid')
            if uid is not None and uid != '':  
                user.uid = uid
                
            dob = body.get('dob')   
            if dob is not None and dob != '':
                try:
                    user.dob = datetime.strptime(dob, '%Y-%m-%d').date()
                except:
                    return {
                        "message": f"Date of birth format error {dob}, must be yyyy-mm-dd",
                        "data": None,
                        "error": "Bad request",
                    }, 400

            ''' Commit changes to the database '''
            user.update()
            return jsonify(user.read())
        
        @token_required("Admin")
        def delete(self): # Delete Method
            body = request.get_json()
            uid = body.get('uid')
            user = User.query.filter_by(_uid=uid).first()
            if user is None:
                return {'message': f'User {uid} not found'}, 404
            json = user.read()
            user.delete() 
            # 204 is the status code for delete with no json response
            return f"Deleted user: {json}", 204 # use 200 to test with Postman
         
    class _Security(Resource):
        def post(self):
            try:
                body = request.get_json()
                if not body:
                    return {
                        "message": "Please provide user details",
                        "data": None,
                        "error": "Bad request"
                    }, 400
                ''' Get Data '''
                uid = body.get('uid')
                if uid is None:
                    return {'message': f'User ID is missing'}, 401
                password = body.get('password')
                
                ''' Find user '''
                user = User.query.filter_by(_uid=uid).first()
                if user is None or not user.is_password(password):
                    return {'message': f"Invalid user id or password"}, 401
                if user:
                    try:
                        token = jwt.encode(
                            {"_uid": user._uid},
                            current_app.config["SECRET_KEY"],
                            algorithm="HS256"
                        )
                        resp = Response("Authentication for %s successful" % (user._uid))
                        resp.set_cookie(current_app.config["JWT_TOKEN_NAME"], 
                                token,
                                max_age=3600,
                                secure=True,
                                httponly=True,
                                path='/',
                                samesite='None'  # This is the key part for cross-site requests

                                # domain="frontend.com"
                                )
                        return resp
                    except Exception as e:
                        return {
                            "error": "Something went wrong",
                            "message": str(e)
                        }, 500
                return {
                    "message": "Error fetching auth token!",
                    "data": None,
                    "error": "Unauthorized"
                }, 404
            except Exception as e:
                return {
                        "message": "Something went wrong!",
                        "error": str(e),
                        "data": None
                }, 500

            
    # building RESTapi endpoint
    api.add_resource(_ID, '/id')
    api.add_resource(_CRUD, '/users')
    api.add_resource(_Security, '/authenticate')
    