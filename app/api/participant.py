from flask import Blueprint, request, jsonify
from app import db, app
from app.models.board import Board
from app.models.participant import Participant
from app.schema.participant import participant_schema, participants_schema
from flask_cors import CORS
import base62

participants = Blueprint('participants', __name__, url_prefix='/api/v1/boards/<board_code>/participants')
CORS(participants, resources={r"/api/*": {"origins": app.config.get('CORS_ORIGINS')}})

@participants.route('', methods=["POST"])
def create_participants(board_code):

    try:
        is_valid = db.session.query(Board)\
        .filter(Board.code == board_code)\
        .first()

        if is_valid:
            name = request.json['name']
            participant = Participant(name=name, board_id=is_valid.id)
            participant.code = base62.encode(1111111)

            db.session.add(participant)
            db.session.commit()
            return participant_schema.dump(participant)
        else:
            raise Exception('404')
    except ValueError:
        return ValueError

@participants.route('', methods=["GET"])
def list_participants(board_code):
    participants = db.session.query(Participant)\
        .filter(Participant.code == board_code)\
        .all()

    return jsonify(participants_schema.dump(participants))

@participants.route('/<id>', methods=["DELETE"])
def remove_participants_by_id(id, board_id):
    participant = db.session.query(Participant)\
        .filter(Participant.board_id == board_id)\
        .filter(Participant.id == id)\
        .first()

    db.session.delete(participant)
    db.session.commit()

    return ('', 204)

@participants.route('/<id>/name', methods=["PUT"])
def modify_participants_by_id(id, board_id):
    participant = db.session.query(Participant)\
        .filter(Participant.board_id == board_id)\
        .filter(Participant.id == id)\
        .first()

    name = request.json['name']
    participant.name = name

    db.session.commit()

    return jsonify(participant_schema.dump(participant))