from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import (create_user, get_all_routes, search_routes)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    routelist = get_all_routes()
    return render_template('index.html', routes = routelist)

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})


@index_views.route('/search', methods = ['POST'])
def search():
    word = request.form
    found = search_routes(word["search_term"])
    return render_template('index.html', routes = found)
    # print("this is the search function call " + word["search_term"])
    # return word["search_term"]