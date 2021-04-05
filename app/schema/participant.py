from app import ma
from app.models.participant import Participant

class ParticipantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Participant
        fields = ('code', 'name', 'score')

participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)