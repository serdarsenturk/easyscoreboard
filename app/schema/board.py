from app import ma
from app.models.board import Board
from app.schema.participant import ParticipantSchema

class BoardSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Board

    code = ma.auto_field()
    name = ma.auto_field()
    participants = ma.Nested(ParticipantSchema, many=True)

board_schema = BoardSchema()