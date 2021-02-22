from flask import Blueprint, jsonify

from app.models.scoreboard import ScoreBoard

url = Blueprint('url', __name__, url_prefix='/')

@url.route('/')
def homeView():
    return "<h1>Welcome to Easy Score Board.</h1>"

@url.route('api/v1/hello', methods=["GET"])
def readById():
    score_board = ScoreBoard.query.get(1)
    return jsonify(id=score_board.id, name=score_board.name)