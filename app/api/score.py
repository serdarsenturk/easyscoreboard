from flask import Blueprint, jsonify, request
from pusher import Pusher
from werkzeug.exceptions import NotFound
from .. import db
from app.models.board import Board
from app.models.participant import Participant
from app.schema.participant import participant_schema
from flask_cors import CORS

scores = Blueprint('scores', __name__, url_prefix='/api/v1/boards/<board_code>/participants/<participant_code>/score')
CORS(scores, resources={r"/api/*": {"origins": 'http://localhost:3000'}})

@scores.route('', methods=["PUT"])
def add_score_by_code(participant_code, board_code):
    board = db.session.query(Board) \
        .filter(Board.code == board_code) \
        .first()

    if board is None:
        raise NotFound()

    increment = request.json['increment']

    participant = db.session.query(Participant) \
        .filter(Participant.board_id == board.id) \
        .filter(Participant.code == participant_code) \
        .first()
    participant.score += increment

    db.session.commit()
    return jsonify(participant_schema.dump(participant))
