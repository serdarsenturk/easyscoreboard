from app import ma
from app.models.scoreboard import ScoreBoard

class ScoreBoardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ScoreBoard

score_board_schema = ScoreBoardSchema()
score_boards_schema = ScoreBoardSchema(many=True)