from marshmallow import fields
from app import ma

class ParticipantSchema(ma.SQLAlchemyAutoSchema):
    code = fields.Str()
    name = fields.Str()
    score = fields.Int()

participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)