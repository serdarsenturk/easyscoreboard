from app import db

class ScoreBoard(db.Model):
    __tablename__ = 'score_boards'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
