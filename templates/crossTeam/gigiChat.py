"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect
from crud3.model import Users

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_gigiChat = Blueprint('gigiChat', __name__,
                         url_prefix='/crossTeam',
                         template_folder='crossTeam',
                         static_folder='static',
                         static_url_path='../../static')

# Default URL
@app_gigiChat.route('/')
def gigiChat():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crossTeam/gigiChat.html", table=users_all())


# CRUD create/add
@app_gigiChat.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Users(
            request.form.get("name"),
            request.form.get("email"),
            request.form.get("message"),
        )
        po.create()
    return redirect(url_for('crossTeam.gigiChat'))


# CRUD read
@app_gigiChat.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        userid = request.form.get("userid")
        po = user_by_id(userid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("crossTeam/gigiChat.html", table=table)


# CRUD update
@app_gigiChat.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        userid = request.form.get("userid")
        name = request.form.get("name")
        po = user_by_id(userid)
        if po is not None:
            po.update(name)
    return redirect(url_for('crossTeam.gigiChat'))

