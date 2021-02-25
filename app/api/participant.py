from flask import Blueprint, request, jsonify
from app import db
from app.models.participant import Participant
from app.schema.participant import participant_schema, participants_schema

participants = Blueprint('participants', __name__, url_prefix='/api/v1/scoreboards/participants')

@participants.route('', methods=["POST"])
def create_participants():
    name = request.json['name']
    board_id = request.json['board_id']

    participant = Participant(name=name, board_id=board_id)

    db.session.add(participant)
    db.session.commit()
    return participant_schema.dump(participant)

@participants.route('/<board_id>', methods=["GET"])
def list_participants(board_id):
    participants = db.session.query(Participant.name, Participant.score).join(ScoreBoard).filter(ScoreBoard.id == board_id)

    return jsonify(participants_schema.dump(participants))

@participants.route('/<id>', methods=["DELETE"])
def remove_participants_by_id(id):
    participant = Participant.query.get(id)
    db.session.delete(participant)
    db.session.commit()

    return jsonify(participant_schema.dump(participant))

@participants.route('/<id>', methods=["PUT"])
def modify_participants_by_id(id):
    participant = Participant.query.get(id)
    name = request.json['name']

    participant.name = name

    db.session.commit()

    return jsonify(participant_schema.dump(participant))