from App.models import Route
from App.database import db



def create_route(origin, destination):
    newroute = Route(origin = origin, destination =destination)
    db.session.add(newroute)
    db.session.commit()
    return newroute

def get_all_routes():
    return Route.query.all()