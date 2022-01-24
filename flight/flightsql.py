from __init__ import db
from flight.flightmodel import Flights
import random


# this is method called by frontend, it has been randomized between Alchemy and Native SQL for fun
def flights_all():
    if random.randint(0, 1) == 0:
        table = flights_all_alc()
    else:
        table = flights_all_sql()
    return table


# SQLAlchemy extract all users from database
def flights_all_alc():
    table = Flights.query.all()
    json_ready = [peep.read() for peep in table]
    return json_ready


# Native SQL extract all users from database
def flights_all_sql():
    table = db.session.execute('select * from flights')
    json_ready = sqlquery_2_list(table)
    return json_ready


# SQLAlchemy extract users from database matching term
def flights_ilike(term):
    """filter Users table by term into JSON list (ordered by User.name)"""
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Flights.query.order_by(Flights.name).filter((Flights.name.ilike(term)) | (Flights.departingLocation.ilike(term)))
    return [peep.read() for peep in table]


# SQLAlchemy extract single user from database matching ID
def flight_by_id(flightid):
    """finds User in table matching userid """
    return Flights.query.filter_by(flightID=flightid).first()


# SQLAlchemy extract single user from database matching departingLocation
def flight_by_departingLocation(departingLocation):
    """finds User in table matching departingLocation """
    return Flights.query.filter_by(departingLocation=departingLocation).first()


# ALGORITHM to convert the results of an SQL Query to a JSON ready format in Python
def sqlquery_2_list(rows):
    out_list = []
    keys = rows.keys()  # "Keys" are the columns of the sql query
    for values in rows:  # "Values" are rows within the SQL database
        row_dictionary = {}
        for i in range(len(keys)):  # This loop lines up K, V pairs, same as JSON style
            row_dictionary[keys[i]] = values[i]
        row_dictionary["query"] = "by_sql"  # This is for fun a little watermark
        out_list.append(row_dictionary)  # Finally we have a out_list row
    return out_list


# Test queries
if __name__ == "__main__":
    for i in range(1):
        print(flights_all())
