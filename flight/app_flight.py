"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response

from flight.flightsql import *

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_flight = Blueprint('flight', __name__,
                     url_prefix='/flight',
                     template_folder='templates/flight/',
                     static_folder='static',
                     static_url_path='static')

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes for CRUD (Blueprint)
"""


# Default URL
@app_flight.route('/')
def flight():
    """obtains all Users from table and loads Admin Form"""
    return render_template("flight.html", table=flights_all())


# CRUD create/add
@app_flight.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Flights(
            request.form.get("name"),
            request.form.get("departingLocation"),
            request.form.get("arrivalLocation"),
            request.form.get("departingTime"),
            request.form.get("arrivalTime")
        )
        po.create()
    return redirect(url_for('flight.flight'))


# CRUD read
@app_flight.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        flightid = request.form.get("flightid")
        po = flight_by_id(flightid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("flight.html", table=table)


# CRUD update
@app_flight.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        flightid = request.form.get("flightid")
        name = request.form.get("name")
        po = flight_by_id(flightid)
        if po is not None:
            po.update(name)
    return redirect(url_for('flight.flight'))


# CRUD delete
@app_flight.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        flightid = request.form.get("flightid")
        po = flight_by_id(flightid)
        if po is not None:
            po.delete()
    return redirect(url_for('flight.flight'))


# Search Form
@app_flight.route('/search/')
def search():
    """loads form to search Users data"""
    return render_template("flightsearch.html")


# Search request and response
@app_flight.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(flights_ilike(term)), 200)
    return response
