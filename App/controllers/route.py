from App.models import Route
from App.database import db



def create_route(origin, destination, vehicle, departure, arrival, distance):
    newroute = Route(origin = origin, destination =destination, vehicle = vehicle, departure = departure, arrival = arrival, distance = distance)
    db.session.add(newroute)
    db.session.commit()
    return newroute

# def create_route(origin, destination, departure, arrival):
#     newroute = Route(origin = origin, destination =destination, departure = departure, arrival= arrival)
#     db.session.add(newroute)
#     db.session.commit()

def get_all_routes():
    return Route.query.all()

def search_routes(search_word):
    return Route.query.filter_by(origin = search_word).all()

def route_filter(filter_word):
    return Route.query.filter_by(vehicle = filter_word).all()

def search_id(id):
    return Route.query.filter_by(id= id).first()