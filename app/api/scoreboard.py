from flask import Blueprint, jsonify, request
from app import db
from app.models.scoreboard import ScoreBoard
from app.schema.scoreboard import scoreboards_schema, scoreboard_schema

scoreboard = Blueprint('scoreboard', __name__, url_prefix='/api/v1/scoreboards')

@scoreboard.route('<id>', methods=["GET"])
def get_scoreboard_by_id(id):
    scoreboard = ScoreBoard.query.get(id)
    return jsonify(scoreboard_schema.dump(scoreboard))

@scoreboard.route('/', methods=["GET"])
def list_scoreboards():
    scoreboards = ScoreBoard.query.all()
    return jsonify(scoreboards_schema.dump(scoreboards))

@scoreboard.route('/', methods=["POST"])
def create_scoreboard():
    name = request.json['name']

    new_scoreboard = ScoreBoard(name=name)

    db.session.add(new_scoreboard)
    db.session.commit()
    return scoreboard_schema.dump(new_scoreboard)

@scoreboard.route('/<id>', methods=["PUT"])
def modify_scoreboard_by_id(id):
    scoreboard = ScoreBoard.query.get(id)
    name = request.json['name']

    scoreboard.name = name

    db.session.commit()
    return scoreboard_schema.dump(scoreboard)