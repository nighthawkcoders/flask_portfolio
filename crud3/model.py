""" database dependencies to support Users db examples """
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate

from __init__ import app

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
# Define variable to define type of database (sqlite), and name and location of myDB.db
dbURI = 'sqlite:///model/myDB.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Users(db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)
    gender = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, email, password, phone, gender):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.gender = gender

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
            db.session.commit()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "gender": self.gender
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, name, password="", phone="", gender=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(password) > 0:
            self.password = password
        if len(phone) > 0:
            self.phone = phone
        if len(gender) > 0:
            self.gender = gender
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
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Users(name='Sonakshi Bhalla', email='sonakshi@example.com', password='123school', phone="8471947575", gender="female")
    u2 = Users(name='Shreya Ahuja', email='shreya@example.com', password='123milo', phone="1111112222", gender="female")
    u3 = Users(name='Khushi Bagri', email='khushi@example.com', password='123khushi', phone="1111113333", gender="female")
    u4 = Users(name='Punnu Sangram', email='punnu@example.com', password='123punnu', phone="1111114444", gender="male")
    u5 = Users(name='John Mortensen', email='jmort1021@gmail.com', password='123qwerty', phone="8587754956", gender="male")
    u6 = Users(name='Bob Fred', email='bobfred1@yahoo.com', password='123bobfred', phone="8587754956", gender="male")
    u7 = Users(name='Anthony Smith', email='anthony@yahoo.com', password='123bobfred', phone="9987679000", gender="male")
    u8 = Users(name='Jake Gregory', email='jake@yahoo.com', password='123gregory', phone="7349327488", gender="male")
# U9 intended to fail as duplicate key
    u9 = Users(name='John Mortensen', email='jmort1021@gmail.com', password='123qwerty', phone="8587754956", gender="male")
    table = [u1, u2, u3, u4, u5, u6, u7, u8, u9]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            db.session.commit()
            print(f"Records exist, duplicate email, or error: {row.email}")


def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()