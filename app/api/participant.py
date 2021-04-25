from flask import Blueprint, request, jsonify
from sqlalchemy import Sequence
from werkzeug.exceptions import NotFound
from app import db, app
from app.models.board import Board
from app.models.participant import Participant
from app.schema.participant import participant_schema, participants_schema
from flask_cors import CORS
import base62
from pusher import Pusher

participants = Blueprint('participants', __name__, url_prefix='/api/v1/boards/<board_code>/participants')
CORS(participants, resources={r"/api/*": {"origins": app.config.get('CORS_ORIGINS')}})

pusher = Pusher(
    app_id=app.config.get('PUSHER_APP_ID'),
    key=app.config.get('PUSHER_KEY'),
    secret=app.config.get('PUSHER_SECRET'),
    cluster='eu',
    ssl=True
)

@participants.route('', methods=["POST"])
def create_participants(board_code):
    board = db.session.query(Board)\
        .filter(Board.code == board_code)\
        .first()

    if board is None:
        raise NotFound()

    name = request.json['name']
    participant = Participant(name=name, board_id=board.id)
    participant.id = db.session.execute(Sequence("participants_id_seq"))
    participant.code = base62.encode(hash(('participants', participant.id)), 8)[-8:]

    db.session.add(participant)
    db.session.commit()

    pusher.trigger(f"board-{board_code}", 'updated', None)

    return participant_schema.dump(participant)

@participants.route('', methods=["GET"])
def list_participants(board_code):
    board = db.session.query(Board) \
        .filter(Board.code == board_code) \
        .first()

    if board is None:
        raise NotFound()

    participant_list = db.session.query(Participant) \
        .filter(Participant.board_id == board.id) \
        .all()

    return jsonify(participants_schema.dump(participant_list))

@participants.route('/<code>', methods=["DELETE"])
def remove_participants_by_code(code, board_code):
    board = db.session.query(Board)\
    .filter(Board.code == board_code)\
    .first()

    if board is None:
        raise NotFound()

    participant = db.session.query(Participant) \
        .filter(Participant.board_id == board.id) \
        .filter(Participant.code == code) \
        .first()

    db.session.delete(participant)

    db.session.commit()

    return '', 204

@participants.route('/<code>/name', methods=["PUT"])
def modify_participants_by_code(code, board_code):
    board = db.session.query(Board)\
    .filter(Board.code == board_code)\
    .first()

    if board is None:
        raise NotFound()

    participant = db.session.query(Participant) \
        .filter(Participant.board_id == board.id) \
        .filter(Participant.code == code) \
        .first()

    name = request.json['name']
    participant.name = name

    db.session.commit()

    return jsonify(participant_schema.dump(participant))

