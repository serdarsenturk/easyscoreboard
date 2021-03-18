from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from pusher import Pusher
from app import db
from app.models.participant import Participant
from app.schema.participant import participant_schema

scores = Blueprint('scores', __name__, url_prefix='/api/v1/boards/<board_id>/participants/<id>/score')
CORS(scores)

pusher = Pusher(
    app_id='1173498',
    key='4d834764c992c4d8e8d0',
    secret='73f383f850642ccd16ae',
    cluster='eu',
    ssl=True
)

@scores.route('', methods=["PUT"])
@cross_origin(supports_credentials=True)
def add_score_by_id(id, board_id):
    participant = db.session.query(Participant)\
        .filter(Participant.board_id == board_id)\
        .filter(Participant.id == id)\
        .first()

    increment = request.json['increment']
    participant.score += increment  # Increment to score by `increment` variable where come from function parameter

    db.session.commit()

    return jsonify(participant_schema.dump(participant))