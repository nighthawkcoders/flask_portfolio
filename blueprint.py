from flask import Blueprint

blueprint = Blueprint('example_blueprint', __name__)

@blueprint.route('/sonakshi')
def sonakshi():
    return render_template("sonakshi.html")