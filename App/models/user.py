from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username



class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(120), nullable = False)   
    destination = db.Column(db.String(120), nullable = False)
    departure = db.Column(db.DateTime(), default = datetime.datetime.utcnow)
    arrival = db.Column(db.DateTime(), default = datetime.datetime.utcnow)
    distance = db.Column(db.Double)
    # name = db.Column(db.String(120), unique=True, nullable=False)
    # map_url = db.Column(db.String(200), nullable=False)#if we dont api then this redundant
    # schedule = db.Column(db.String(200), nullable=False)
    # fare = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return self.origin + " " + self.destination + " " + str(self.departure)

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(2000), nullable=False)
    timestamp = db.Column(db.DateTime(timezone = True), default = datetime.datetime.utcnow)

    def __repr__(self):
        return '<ContactMessage %r>' % self.name
  

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

