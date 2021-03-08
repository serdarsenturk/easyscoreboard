from app import ma
from app.models.board import Board

class BoardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Board
        include_fk = True

board_schema = BoardSchema()
boards_schema = BoardSchema(many=True)