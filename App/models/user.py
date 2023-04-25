from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

import datetime


class UserRoutes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('trips', lazy=True))
    route = db.relationship('Route', backref=db.backref('trips', lazy=True))

    def __init__(self, user_id, route_id):
        self.user_id = user_id
        self.route_id = route_id

    def __repr__(self):
        return f'<{self.id}: {self.user_id}: {self.route_id}: {self.user}: {self: route}>'
    

   

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # userss = db.relationship('UserRoutes', backref = db.backref('users', lazy = 'joined'))

    def __init__(self, username, email, password):
      self.username = username
      self.email = email
      self.set_password(password)
    
    def get_json(self):
      return {
        "id": self.id,
        "username": self.username,
        "email": self.email,
        "password": self.password
      }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def save_route(self, route_id):
        rout = Route.query.get(route_id)
        if rout:
            try:
                saveroute = UserRoute(user_id =self.id, route_id =route_id)
                db.session.add(saveroute)
                db.session.commit()
                return saveroute
            except Exception:
                db.session.rollback()
                return None
        return None

    def get_saved(self):
        return "self.trips.route"
    
    def __repr__(self):
        return f'<User {self.username} - {self.email}>'


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(120), nullable = False)   
    destination = db.Column(db.String(120), nullable = False)
    vehicle = db.Column(db.String(30), nullable = False, default = "Taxi")
    departure = db.Column(db.String(120))
    arrival = db.Column(db.String(120))
    distance = db.Column(db.Double)
    # name = db.Column(db.String(120), unique=True, nullable=False)
    # map_url = db.Column(db.String(200), nullable=False)#if we dont api then this redundant
    # schedule = db.Column(db.String(200), nullable=False)
    # fare = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return self.origin + " " + self.destination + " " + str(self.departure) + "  "+ str(self.id)

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

