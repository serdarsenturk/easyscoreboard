from marshmallow import fields
from app import ma
from app.schema.participant import ParticipantSchema

class BoardSchema(ma.SQLAlchemyAutoSchema):
    name = fields.Str()
    code = fields.Str()
    participants = fields.Nested(ParticipantSchema, many=True)

board_schema = BoardSchema()