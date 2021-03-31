from flask import Blueprint, jsonify
from flask_cors import CORS, cross_origin
from flask_wtf.csrf import generate_csrf
from app import app

home = Blueprint('home', __name__)

@home.route('/')
def homeView():
    return "<h1>Welcome to Easy Score Board.</h1>"