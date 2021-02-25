from flask import Blueprint, jsonify

from app import db
from app.models.participant import Participant
from app.schema.participant import participant_schema

scores = Blueprint('scores', __name__, url_prefix='/api/v1/scoreboards/addscore')

@scores.route('/<id>/<int:increment>', methods=["POST"])
def add_score_by_id(id, increment):
    participant = Participant.query.get(id)

    participant.score += increment  # Increment to score by `increment` variable where come from function parameter

    db.session.commit()

    return jsonify(participant_schema.dump(participant))