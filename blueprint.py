from flask import Blueprint, render_template

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/sonakshi')
def sonakshi():
    return render_template("sonakshi.html")