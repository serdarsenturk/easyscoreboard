from flask import Blueprint, jsonify

from app.models.scoreboard import ScoreBoard
from app.schema.scoreboard import score_boards_schema

scoreboard = Blueprint('scoreboard', __name__, url_prefix='/api/v1/')

@scoreboard.route('hello', methods=["GET"])
def readById():
    score_board = ScoreBoard.query.get(1)
    return jsonify(id=score_board.id, name=score_board.name)

@scoreboard.route('scoreboards', methods=["GET"])
