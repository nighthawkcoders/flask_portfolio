""" database dependencies to support Users db examples """
from sqlalchemy.exc import IntegrityError
from __init__ import db

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Pages(db.Model):
    # define the Users schema
    pageID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    display = db.Column(db.String(255), unique=True, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, display):
        self.name = name
        self.display = display

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
            "pageID": self.pageID,
            "name": self.name,
            "display": self.display,
            "query": "by_alc"  # This is for fun, a little watermark
        }

    # CRUD update: updates users name, password, phone
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
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Pages(name='Page 1', display='Link to ex page 1')
    u2 = Pages(name='Page 2', display='Link to ex page 2')
    u3 = Pages(name='Page 3', display='Link to ex page 3')
    u4 = Pages(name='Page 4', display='Link to ex page 4')
    u5 = Pages(name='Page 5', display='Link to ex page 5')
    u6 = Pages(name='Page 6', display='Link to ex page 6')
    u7 = Pages(name='Page 7', display='Link to ex page 7')
    table = [u1, u2, u3, u4, u5, u6, u7]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {row.display}")


def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from pages')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()
