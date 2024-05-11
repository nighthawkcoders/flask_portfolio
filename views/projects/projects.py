from flask import Blueprint, render_template

project_views = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@project_views.route('/portfolio/')
def portfolio():
    return render_template("portfolio.html")

# connects /kangaroos path to render kangaroos.html
@project_views.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")

@project_views.route('/walruses/')
def walruses():
    return render_template("walruses.html")

@project_views.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")