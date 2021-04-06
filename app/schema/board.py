from app import ma
from app.models.board import Board
from app.schema.participant import ParticipantSchema

class BoardSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Board
        fields = ('code', 'name', 'participants')
    participants = ma.Nested(ParticipantSchema, many=True)

board_schema = BoardSchema()