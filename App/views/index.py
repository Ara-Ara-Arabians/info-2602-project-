from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import (create_user, get_all_routes, search_routes, route_filter, create_route, search_id)
from flask_login import login_required


index_views = Blueprint('index_views', __name__, template_folder='../templates')



@index_views.route('/', methods=['GET'])
@login_required
def index_page():

    routelist = get_all_routes()
    return render_template('index.html', routes = routelist)

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/route', methods=['GET'])
@login_required
def route():
    return render_template('route.html')

@index_views.route('/route', methods=['POST'])
@login_required
def add_route():
    origin = request.form['origin']
    destination = request.form['destination']
    vehicle = request.form['vehicle']
    departure = request.form['departure']
    arrival = request.form['arrival']
    distance = request.form['distance']
    departure = str(departure)
    arrival = str(arrival)

    create_route(origin, destination, vehicle, departure, arrival, distance)

    return redirect('/')

@index_views.route('/routeinfo/<int:id>', methods = ['GET'])
@login_required
def get_more_info(id):
    route = search_id(id)
    return render_template('routeinfo.html',  route = route)


@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})


@index_views.route('/search', methods = ['POST'])
@login_required
def search():
    word = request.form
    found = search_routes(word["search_term"])
    return render_template('index.html', routes = found)
    # print("this is the search function call " + word["search_term"])
    # return word["search_term"]

@index_views.route('/filter', methods=['GET'])
@login_required
def filter_routes():
    rsult = request.args.get('filter_button')

    if(rsult == "None"):
        return redirect('/')

    print(str(rsult))
    filtered = route_filter(rsult)
    return render_template('index.html', routes = filtered)
