from app import db

class Participant(db.Model):
    __tablename__ = 'participants'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.VARCHAR(25), nullable=False)
    board_id = db.Column(db.Integer, db.ForeignKey('score_boards.id'), nullable=False)
    score = db.Column(db.Integer, server_default='0')