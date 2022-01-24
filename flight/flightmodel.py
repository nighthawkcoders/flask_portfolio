""" database dependencies to support Users db examples """
from sqlalchemy.exc import IntegrityError
from __init__ import db

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Flights(db.Model):
    # define the Users schema
    flightID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    departingLocation = db.Column(db.String(255), unique=False, nullable=False)
    arrivalLocation = db.Column(db.String(255), unique=True, nullable=False)
    departingTime = db.Column(db.String(255), unique=False, nullable=False)
    arrivalTime = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, departingLocation, arrivalLocation, departingTime, arrivalTime):
        self.name = name
        self.departingLocation = departingLocation
        self.arrivalLocation = arrivalLocation
        self.departingTime = departingTime
        self.arrivalTime = arrivalTime

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "flightID": self.flightID,
            "name": self.name,
            "departingLocation": self.departingLocation,
            "arrivalLocation": self.arrivalLocation,
            "departingTime": self.departingTime,
            "arrivalTime": self.arrivalTime,
            "query": "by_alc"  # This is for fun, a little watermark
        }

    # CRUD update: updates users name, arrivalLocation, departingTime
    # returns self
    def update(self, name):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Table: flights")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Flights(name='American Airlines', departingLocation='San Diego SAN', arrivalLocation='Boston BOS',
                 departingTime="8:30 PM", arrivalTime="8:30 PM")
    u2 = Flights(name='United Airlines', departingLocation='Los Angeles LAX', arrivalLocation='Orlando MCO',
                 departingTime="7:45PM", arrivalTime="8:30 PM")
    u3 = Flights(name='Southwest', departingLocation='San Diego SAN', arrivalLocation='San Francisco SFO',
                 departingTime="1:45PM", arrivalTime="8:30 PM")
    u4 = Flights(name='Delta', departingLocation='Austin AUS', arrivalLocation='Denver DEN',
                 departingTime="1:30PM", arrivalTime="8:30 PM")
    u5 = Flights(name='Alaskan Airlines', departingLocation='Vancouver YVR', arrivalLocation='Seattle SEA',
                 departingTime="2:00PM", arrivalTime="8:30 PM")
    u6 = Flights(name='Spirit', departingLocation='New York JFK', arrivalLocation='Tallahassee TLH',
                 departingTime="11:15 AM", arrivalTime="8:30 PM")
    u7 = Flights(name='Emirates', departingLocation='Dubai DXB', arrivalLocation='Los Angeles LAX',
                 departingTime="10:45 PM", arrivalTime="8:30 PM")
    u8 = Flights(name='Lufthansa', departingLocation='Berlin BML', arrivalLocation='Munich MUC',
                 departingTime="12:30 PM", arrivalTime="8:30 PM")
    u9 = Flights(name='Quantas', departingLocation='Sydney SYD', arrivalLocation='Melbourne MEL',
                 departingTime="3:45 PM", arrivalTime="8:30 PM")
    u10 = Flights(name='British Airways', departingLocation='London LHR', arrivalLocation='Montreal YUL',
                  departingTime="7:00 PM", arrivalTime="8:30 PM")
    u11 = Flights(name='Swiss Air', departingLocation='Zurich ZRH', arrivalLocation='New York JFK',
                  departingTime="9:30 PM", arrivalTime="8:30 PM")
    u12 = Flights(name='Air India', departingLocation='New Delhi DEL', arrivalLocation='San Francisco SFO',
                  departingTime="8:45 AM", arrivalTime="8:30 PM")
    table = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate departingLocation, or error: {row.departingLocation}")


def model_printer():
    print("------------")
    print("Table: flights with SQL query")
    print("------------")
    result = db.session.execute('select * from flights')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()
