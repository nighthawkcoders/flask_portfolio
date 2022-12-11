# Werkzeug is a collection of libraries that can be used to create a WSGI (Web Server Gateway Interface)
# A gateway in necessary as a web server cannot communicate directly with Python.
# In this case, imports are focused on generating hash code to protect passwords.
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from __init__ import db

# Define a User Class/Template
# -- A User is managed one row/record at a time
class User(db.Model):
    # table contains many users
    __tablename__ = 'users'     

    # Define the User table schema
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    uid = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    
    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, name, uid, password):
        self._name = name    # variables with self prefix become part of the object, 
        self._uid = uid
        self.set_password(password)

    # a name getter method, extracts name from object
    @property
    def name(self):
        return self._name
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, name):
        self._name = name
    
    # a getter method, extracts email from object
    @property
    def uid(self):
        return self._uid
    
    # a setter function, allows name to be updated after initial object creation
    @uid.setter
    def uid(self, uid):
        self._uid = uid
        
    # check if uid parameter matches user id in object, return boolean
    def is_uid(self, uid):
        return self._uid == uid
    
    @property
    def password(self):
        return self._password[0:10] + "..." # because of security only show 1st characters

    # update password, this is conventional setter
    def set_password(self, password):
        """Create a hashed password."""
        self._password = generate_password_hash(password, method='sha256')

    # check password parameter versus stored/encrypted password
    def is_password(self, password):
        """Check against hashed password."""
        result = check_password_hash(self._password, password)
        return result
    
    # output content using str(object) in human readable form, uses getter
    def __str__(self):
        return f'name: "{self.name}", id: "{self.uid}", psw: "{self.password}"'

    # output command to recreate the object, uses attribute directly
    def __repr__(self):
        return f'User(name={self._name}, uid={self._uid}, password={self._password})'
    
    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a user object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist user object to User table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read, returns dictionary representation of object
    # returns dictionary
    def read(self):
        return self.__dict__
    
    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, name="", uid="", password=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(uid) > 0:
            self.uid = uid
        if len(password) > 0:
            self.set_password(password)
        db.session.commit()
        return self
    
    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


# tester method to print users
def tester(users, uid, psw):
    result = None
    for user in users:
        # test for match in database
        if user.uid == uid and user.is_password(psw):  # check for match
            print("* ", end="")
            result = user
        # print using __str__ method
        print(str(user))
    return result
        
# Sets up and seed table
def initUsers():
    """Create database and tables"""
    db.create_all()        
    # define user objects
    u1 = User(name='Thomas Edison', uid='toby', password='123toby')
    u2 = User(name='Nicholas Tesla', uid='nick', password='123nick')
    u3 = User(name='Alexander Graham Bell', uid='lex', password='123lex')
    u4 = User(name='Eli Whitney', uid='eli', password='123eli')
    u5 = User(name='Hedy Lemarr', uid='hedy', password='123hedy')

    # put user objects in list for convenience
    users = [u1, u2, u3, u4, u5]
    """Builds user data"""
    for user in users:
        verify_user = user.create()
        print(verify_user)
        
# Looks into database
def testUsers():
    print("---------------------------")
    print("Table: " + User.__tablename__)
    print("Columns: ", User.__table__.columns.keys())
    print("---------------------------")
    print()

    users = User.query
    for user in users:
        print("User" + "-" * 81)
        print(user.read())
        print()
        
if __name__ == "__main__":
    initUsers()
    testUsers()
