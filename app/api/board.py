from flask import Blueprint, jsonify, request
from app import db
from app.models.board import Board
from app.schema.board import boards_schema, board_schema
from flask_cors import cross_origin, CORS

boards = Blueprint('boards', __name__, url_prefix='/api/v1/boards')
CORS(boards)

@boards.route('<id>', methods=["GET"])
@cross_origin(supports_credentials=True)
def get_board_by_id(id):
    board = Board.query.get(id)
    return jsonify(board_schema.dump(board))

@boards.route('/', methods=["GET"])
@cross_origin(supports_credentials=True)
def list_boards():
    boards = Board.query.all()
    return jsonify(boards_schema.dump(boards))

@boards.route('/', methods=["POST"])
@cross_origin(supports_credentials=True)
def create_board():
    name = request.json['name']

    new_board = Board(name=name)

    db.session.add(new_board)
    db.session.commit()
    return board_schema.dump(new_board)

@boards.route('/<id>/name', methods=["PUT"])
@cross_origin(supports_credentials=True)
def modify_board_by_id(id):
    board = Board.query.get(id)
    name = request.json['name']

    board.name = name

    db.session.commit()
    return board_schema.dump(board)