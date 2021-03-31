from flask import Blueprint, jsonify
from flask_cors import CORS
from flask_wtf.csrf import generate_csrf
from app import app

home = Blueprint('home', __name__)
CORS(home, resources={r"/api/*": {"origins": app.config.get('CORS_ORIGINS')}}, supports_credentials=True)

@home.route('/')
def homeView():
    return "<h1>Welcome to Easy Score Board.</h1>"

@home.route('/api/v1/aft')
def AFT():
    token = generate_csrf('serdarsenturk')

    return jsonify({"X-CSRFToken": token})