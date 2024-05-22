from functools import wraps
import jwt
from flask import request, abort
from flask import current_app, g
from model.users import User

def token_required(roles=None):
    '''
    This function is used to guard API endpoints that require authentication.
    Here is how it works:
      1. checks for the presence of a valid JWT token in the request cookie
      2. decodes the token and retrieves the user data
      3. checks if the user data is found in the database
      4. checks if the user has the required role
      5. set the current_user in the global context (Flask's g object)
      6. returns the decorated function if all checks pass
    Here are some possible error responses:    
      A. 401 / Unauthorized: token is missing or invalid
      B. 403 / Forbidden: user has insufficient permissions
      C. 500 / Internal Server Error: something went wrong with the token decoding
    '''
    def decorator(func_to_guard):
        @wraps(func_to_guard)
        def decorated(*args, **kwargs):
            token = request.cookies.get(current_app.config["JWT_TOKEN_NAME"])
            if not token:
                return {
                    "message": "Authentication Token is missing!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
            try:
                # Decode the token and retrieve the user data
                data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
                current_user = User.query.filter_by(_uid=data["_uid"]).first()
                if current_user is None:
                    return {
                        "message": "Invalid Authentication token!",
                        "data": None,
                        "error": "Unauthorized"
                    }, 401
                    
                # Check user has the required role, when role is required 
                if roles and current_user.role not in roles:
                    return {
                        "message": "Insufficient permissions. Required roles: {}".format(roles),
                        "data": None,
                        "error": "Forbidden"
                    }, 403
                    
                # Success finding user and (optional) role
                # Set the current_user in the global context
                # Flask's g object is a global object that lasts for the duration of the request
                # The g.current_user can be referenced in decorated function 
                g.current_user = current_user
            
            # Error exception is for unknown jwt.decode errors 
            except Exception as e:
                return {
                    "message": "Something went wrong decoding the token!",
                    "data": None,
                    "error": str(e)
                }, 500

            # Success, return to the decorated function
            # func_to_guard is the function with the @token_required
            # func_to_guard returns with the original function arguments
            return func_to_guard(*args, **kwargs)

        return decorated

    return decorator
