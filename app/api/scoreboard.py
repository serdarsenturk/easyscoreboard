from flask import Blueprint, jsonify

from app.models.scoreboard import ScoreBoard

scoreboard = Blueprint('scoreboard', __name__, url_prefix='/api/v1/')

@scoreboard.route('hello', methods=["GET"])
def readById():
    score_board = ScoreBoard.query.get(1)
    return jsonify(id=score_board.id, name=score_board.name)