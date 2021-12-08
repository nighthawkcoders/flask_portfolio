from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

# Fun Facts API
nathan_fun = ["programming", "League of Legends", "golf", "VOCALOID", "rhythm games", "game development", "web development"]
daniel_fun = ["Running Track", "Video Games", "Wakeboarding", "Lofi", "Climbing/Hiking", "Attempt to learn violin"]
reem_fun = ["Soccer", "Selling my soul to Riot Games", "Playing games", "Hanging out with friends", "Engineering"]
jacob_fun = ["Memes", "Video games", "Karate", "Engineering", "Driving"]
james_fun = ["soccer", "games"]

@api_bp.route("/nathan")
def get_nathan_fun():
    return jsonify(nathan_fun)

@api_bp.route("/jacob")
def get_jacob_fun():
    return jsonify(jacob_fun)

@api_bp.route("/reem_fun")
def get_reem_fun():
    return jsonify(reem_fun)

@api_bp.route("/james")
def get_james_fun():
    return jsonify(james_fun)

@api_bp.route("/danielabout")
def get_daniel_fun():
    return jsonify(daniel_fun)