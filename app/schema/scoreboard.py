from app import ma
from app.models.scoreboard import ScoreBoard

class ScoreBoardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ScoreBoard

scoreboard_schema = ScoreBoardSchema()
scoreboards_schema = ScoreBoardSchema(many=True)

