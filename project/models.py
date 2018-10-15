from project import db

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User %d %s' % (self.id, self.username)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    year = db.Column(db.Integer)
    month = db.Column(db.String)
    picture = db.Column(db.String)
    description = db.Column(db.String)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    message = db.Column(db.String)

class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String)
    requirements = db.Column(db.String)


# TODO: Create your other models here
class YourModel(db.Model):
    
    __tablename__ = "yourmodel"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # fill in the rest of your fields and methods!
