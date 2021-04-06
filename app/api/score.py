from flask import Blueprint, jsonify, request
from pusher import Pusher
from werkzeug.exceptions import NotFound
from app import db, app
from app.models.board import Board
from app.models.participant import Participant
from app.schema.participant import participant_schema
from flask_cors import CORS

scores = Blueprint('scores', __name__, url_prefix='/api/v1/boards/<board_code>/participants/<participant_code>/score')
CORS(scores, resources={r"/api/*": {"origins": app.config.get('CORS_ORIGINS')}})

pusher = Pusher(
    app_id=app.config.get('PUSHER_APP_ID'),
    key=app.config.get('PUSHER_KEY'),
    secret=app.config.get('PUSHER_SECRET'),
    cluster='eu',
    ssl=True
)

@scores.route('', methods=["PUT"])
def add_score_by_code(participant_code, board_code):
    board = db.session.query(Board) \
        .filter(Board.code == board_code) \
        .first()

    if is_valid:
        increment = request.json['increment']

        participant = db.session.query(Participant) \
            .filter(Participant.board_id == is_valid.id) \
            .filter(Participant.code == participant_code) \
            .first()
        participant.score += increment

        db.session.commit()
        pusher.trigger(f"participant-{participant.code}", 'score-updated', participant.score)
        return jsonify(participant_schema.dump(participant))
    else:
        raise Exception('404')