from app import ma
from app.models.participant import Participant


class ParticipantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Participant

participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)