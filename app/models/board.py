from app import db
from app.models.participant import Participant

class Board(db.Model):
    __tablename__ = 'boards'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    participants = db.relationship("Participant", backref="participant")
