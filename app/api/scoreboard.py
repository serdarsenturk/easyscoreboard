from flask import Blueprint, jsonify, request
from app import db
from app.models.participant import Participant
from app.models.scoreboard import ScoreBoard
from app.schema.participant import participant_schema, participants_schema
from app.schema.scoreboard import scoreboards_schema, scoreboard_schema

scoreboard = Blueprint('scoreboard', __name__, url_prefix='/api/v1/scoreboards')

@scoreboard.route('<id>', methods=["GET"])
def get_scoreboard_by_id(id):
    scoreboard = ScoreBoard.query.get(id)
    return jsonify(scoreboard_schema.dump(scoreboard))

@scoreboard.route('/', methods=["GET"])
def list_scoreboards():
    scoreboards = ScoreBoard.query.all()
    return jsonify(scoreboards_schema.dump(scoreboards))

@scoreboard.route('/', methods=["POST"])
def create_scoreboard():
    name = request.json['name']

    new_scoreboard = ScoreBoard(name=name)

    db.session.add(new_scoreboard)
    db.session.commit()
    return scoreboard_schema.dump(new_scoreboard)

@scoreboard.route('/<id>', methods=["PUT"])
def modify_scoreboard_by_id(id):
    scoreboard = ScoreBoard.query.get(id)
    name = request.json['name']

    scoreboard.name = name

    db.session.commit()
    return scoreboard_schema.dump(scoreboard)


@scoreboard.route('/participants', methods=["POST"])
def create_participants():
    name = request.json['name']
    board_id = request.json['board_id']

    participant = Participant(name=name, board_id=board_id)

    db.session.add(participant)
    db.session.commit()
    return participant_schema.dump(participant)

@scoreboard.route('/participants/<board_id>', methods=["GET"])
def list_participants(board_id):
    participants = db.session.query(Participant.name).join(ScoreBoard).filter(ScoreBoard.id == board_id)

    return jsonify(participants_schema.dump(participants))

@scoreboard.route('/participants/<id>', methods=["DELETE"])
def remove_participants_by_id(id):
    participant = Participant.query.get(id)
    db.session.delete(participant)
    db.session.commit()

    return jsonify(participant_schema.dump(participant))

@scoreboard.route('participants/<id>', methods=["PUT"])
def modify_participants_by_id(id):
    participant = Participant.query.get(id)
    name = request.json['name']

    participant.name = name

    db.session.commit()

    return jsonify(participant_schema.dump(participant))

