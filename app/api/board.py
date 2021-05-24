from flask import Blueprint, jsonify, request
from sqlalchemy import Sequence
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from app import db, app
from app.models.board import Board
from flask_cors import CORS
from app.schema.board import board_schema
import base62
from pusher import Pusher

boards = Blueprint('boards', __name__, url_prefix='/api/v1/boards')
CORS(boards, resources={r"/api/*": {"origins": app.config.get('CORS_ORIGINS')}})

pusher = Pusher(
    app_id=app.config.get('PUSHER_APP_ID'),
    key=app.config.get('PUSHER_KEY'),
    secret=app.config.get('PUSHER_SECRET'),
    cluster='eu',
    ssl=True
)

def generate_board_code(board):
    try:
        board.id = db.session.execute(Sequence("boards_id_seq"))
        board.code = base62.encode(hash(('boards', board.id)), 8)[-8:]

        db.session.add(board)
        db.session.commit()

        return board
    except IntegrityError:
        db.session.rollback()
        return generate_board_code(board)

@boards.route('<code>', methods=["GET"])
def get_board_by_code(code):
    board = db.session.query(Board) \
        .filter(Board.code == code) \
        .first()

    if board is None:
        raise NotFound()

    return jsonify(board_schema.dump(board))

@boards.route('/', methods=["POST"])
def create_board():
    name = request.json['name']

    new_board = Board(name=name)

    return board_schema.dump(generate_board_code(new_board))

@boards.route('/<code>/name', methods=["PUT"])
def modify_board_by_code(code):
    board = db.session.query(Board)\
        .filter(Board.code == code)\
        .first()

    if board is None:
        raise NotFound()

    name = request.json['name']

    board.name = name

    db.session.commit()

    pusher.trigger(f"board-{code}", 'updated', None)

    return board_schema.dump(board)