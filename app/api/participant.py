from flask import Blueprint, request, jsonify
from flask_cors import CORS
from app import db
from app.models.participant import Participant
from app.schema.participant import participant_schema, participants_schema

participants = Blueprint('participants', __name__, url_prefix='/api/v1/boards/<board_id>/participants')
CORS(participants)

@participants.route('', methods=["POST"])
def create_participants(board_id):
    name = request.json['name']

    participant = Participant(name=name, board_id=board_id)

    db.session.add(participant)
    db.session.commit()
    return participant_schema.dump(participant)

@participants.route('', methods=["GET"])
def list_participants(board_id):
    participants = db.session.query(Participant.id, Participant.score)\
        .filter(Participant.board_id == board_id)\
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