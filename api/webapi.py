import random

from flask import Blueprint, jsonify
# webapi
api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

locations = []
location_list = [
    "words",
    "more words"
]


def _find_next_id():
    return max(locations["id"] for location in locations) + 1


def _init_locations():
    id = 1
    for location in location_list:
        locations.append({"id": id, "location": location, "var": 0, "var1": 0})
        id += 1


@api_bp.route('/location')
def get_location():
    if len(locations) == 0:
        _init_locations()
    return jsonify(random.choice(locations))


@api_bp.route('/locations')
def get_locations():
    if len(locations) == 0:
        _init_locations()
    return jsonify(locations)


if __name__ == "__main__":
    print(random.choice(location_list))
