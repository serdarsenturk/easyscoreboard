from flask import Blueprint, jsonify, request
from app import db
from app.models.scoreboard import ScoreBoard
from app.schema.scoreboard import scoreboards_schema, scoreboard_schema

scoreboard = Blueprint('scoreboard', __name__, url_prefix='/api/v1/scoreboards')

@scoreboard.route('<id>', methods=["GET"])
def readById(id):
    score_board = ScoreBoard.query.get(id)
    return jsonify(scoreboard_schema.dump(score_board))

@scoreboard.route('/', methods=["GET"])
def return_scoreboards():
    scoreboards = ScoreBoard.query.all()
    return jsonify(scoreboards_schema.dump(scoreboards))

@scoreboard.route('/', methods=["POST"])
def post_scoreboards():
    name = request.json['name']

    new_scoreboard = ScoreBoard(name=name)

    db.session.add(new_scoreboard)
    db.session.commit()
    return scoreboard_schema.dump(new_scoreboard)

