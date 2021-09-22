from flask import Blueprint, render_template
from algorithm.image import image_data

starter_bp = Blueprint('starter', __name__,
                       url_prefix='/starter',
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='assets')

@starter_bp.route('/rgb/')
def rgb():
    return render_template('walruses.html', images=image_data())