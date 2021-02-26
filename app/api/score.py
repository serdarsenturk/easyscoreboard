from flask import Blueprint, jsonify, request
from app import db
from app.models.participant import Participant
from app.models.scoreboard import ScoreBoard
from app.schema.participant import participant_schema

scores = Blueprint('scores', __name__, url_prefix='/api/v1/scoreboards/<board_id>/participants/<id>/score')

@scores.route('', methods=["PUT"])
def add_score_by_id(id, board_id):
    participant = db.session.query(Participant)\
        .filter(ScoreBoard.id == board_id)\
        .filter(Participant.id == id)\
        .first()

    increment = request.json['increment']
    participant.score += increment  # Increment to score by `increment` variable where come from function parameter

    db.session.commit()

    return jsonify(participant_schema.dump(participant))