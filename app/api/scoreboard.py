from flask import Blueprint, jsonify

from app.models.scoreboard import ScoreBoard
from app.schema.scoreboard import score_boards_schema, score_board_schema

scoreboard = Blueprint('scoreboard', __name__, url_prefix='/api/v1/')

@scoreboard.route('scoreboards/<id>', methods=["GET"])
def readById(id):
    score_board = ScoreBoard.query.get(id)
    return jsonify(score_board_schema.dump(score_board))

@scoreboard.route('scoreboards', methods=["GET"])
def return_score_boards():
    score_boards = ScoreBoard.query.all()
    return jsonify(score_boards_schema.dump(score_boards))