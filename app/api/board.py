from flask import Blueprint, jsonify, request
from app import db, app
from app.models.board import Board
from app.schema.board import boards_schema, board_schema
from flask_cors import CORS

boards = Blueprint('boards', __name__, url_prefix='/api/v1/boards')
CORS(boards, resources={r"/api/*": {"origins": app.config.get('CORS_ORIGINS')}})

@boards.route('<id>', methods=["GET"])
def get_board_by_id(id):
    board = Board.query.get(id)
    return jsonify(board_schema.dump(board))

@boards.route('/', methods=["GET"])
def list_boards():
    boards = Board.query.all()
    return jsonify(boards_schema.dump(boards))

@boards.route('/', methods=["POST"])
def create_board():
    name = request.json['name']

    new_board = Board(name=name)

    db.session.add(new_board)
    db.session.commit()
    return board_schema.dump(new_board)

@boards.route('/<id>/name', methods=["PUT"])
def modify_board_by_id(id):
    board = Board.query.get(id)
    name = request.json['name']

    board.name = name

    db.session.commit()
    return board_schema.dump(board)