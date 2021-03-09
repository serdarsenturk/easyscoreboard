from marshmallow import fields

from app import ma
from app.schema.participant import ParticipantSchema


class BoardSchema(ma.SQLAlchemyAutoSchema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    participants = fields.Nested(ParticipantSchema, many=True)

board_schema = BoardSchema()
boards_schema = BoardSchema(many=True)