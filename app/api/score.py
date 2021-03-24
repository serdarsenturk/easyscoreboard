from flask import Blueprint, jsonify, request
from pusher import Pusher
from app import db, app
from app.models.participant import Participant
from app.schema.participant import participant_schema
from flask_cors import CORS

scores = Blueprint('scores', __name__, url_prefix='/api/v1/boards/<board_id>/participants/<id>/score')
CORS(scores, resources={r"/api/*": {"origins": app.config.get('ORIGINS')}})

pusher = Pusher(
    app_id=app.config.get('PUSHER_APP_ID'),
    key=app.config.get('PUSHER_KEY'),
    secret=app.config.get('PUSHER_SECRET'),
    cluster='eu',
    ssl=True
)

@scores.route('', methods=["PUT"])
def add_score_by_id(id, board_id):
    participant = db.session.query(Participant)\
        .filter(Participant.board_id == board_id)\
        .filter(Participant.id == id)\
        .first()

    increment = request.json['increment']

    participant.score += increment

    db.session.commit()
    pusher.trigger(f"participant-{participant.id}", 'score-updated', participant.score)
    return jsonify(participant_schema.dump(participant))