"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response

from page.pagesql import *

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_page = Blueprint('page', __name__,
                     url_prefix='/page',
                     template_folder='templates/page/',
                     static_folder='static',
                     static_url_path='static')

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes for CRUD (Blueprint)
"""


# Default URL
@app_page.route('/')
def page():
    """obtains all Users from table and loads Admin Form"""
    return render_template("page.html", table=pages_all())


# crud create/add
@app_page.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Pages(
            request.form.get("name"),
            request.form.get("display"),
        )
        po.create()
    return redirect(url_for('page.page'))


# CRUD read
@app_page.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        pageid = request.form.get("pageid")
        po = page_by_id(pageid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("page.html", table=table)


# cryd update
@app_page.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        pageid = request.form.get("pageid")
        name = request.form.get("name")
        po = page_by_id(pageid)
        if po is not None:
            po.update(name)
    return redirect(url_for('page.page'))


# page delete
@app_page.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        pageid = request.form.get("pageid")
        po = page_by_id(pageid)
        if po is not None:
            po.delete()
    return redirect(url_for('page.page'))


# Search Form
@app_page.route('/search/')
def search():
    """loads form to search Users data"""
    return render_template("pagesearch.html")


# Search request and response
@app_page.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(pages_ilike(term)), 200)
    return response
