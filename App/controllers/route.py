from App.models import Route
from App.database import db



def create_route(origin, destination):
    newroute = Route(origin = origin, destination =destination)
    db.session.add(newroute)
    db.session.commit()
    return newroute

# def create_route(origin, destination, departure, arrival):
#     newroute = Route(origin = origin, destination =destination, departure = departure, arrival= arrival)
#     db.session.add(newroute)
#     db.session.commit()

def get_all_routes():
    return Route.query.all()