from app import ma
from app.models.scoreboard import ScoreBoard, Participant


class ScoreBoardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ScoreBoard

class ParticipantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Participant

scoreboard_schema = ScoreBoardSchema()
scoreboards_schema = ScoreBoardSchema(many=True)

participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)