from app import ma
from app.models.participant import Participant

class ParticipantSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Participant

    code = ma.auto_field()
    name = ma.auto_field()
    score = ma.auto_field()

participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)