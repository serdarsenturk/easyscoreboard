import os
from flask import Blueprint, jsonify, request
from pusher import Pusher
from app import db
from app.models.participant import Participant
from app.schema.participant import participant_schema

scores = Blueprint('scores', __name__, url_prefix='/api/v1/boards/<board_id>/participants/<id>/score')

pusher = Pusher(
    app_id=os.environ.get('PUSHER_APP_ID'),
    key=os.environ.get('PUSHER_KEY'),
    secret=os.environ.get('PUSHER_SECRET'),
    cluster=os.environ.get('PUSHER_CLUSTER'),
    ssl=True
)

@scores.route('', methods=["PUT"])
def add_score_by_id(id, board_id):
    participant = db.session.query(Participant)\
        .filter(Participant.board_id == board_id)\
        .filter(Participant.id == id)\
        .first()

    increment = request.json['increment']
    participant.score += increment  # Increment to score by `increment` variable where come from function parameter

    db.session.commit()
    pusher.trigger(f"participant-{participant.id}", 'score-updated', participant.score)
    return jsonify(participant_schema.dump(participant))