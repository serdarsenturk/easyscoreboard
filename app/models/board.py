from .. import db

class Board(db.Model):
    __tablename__ = 'boards'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    code = db.Column(db.String(8), nullable=False, unique=True, index=True)
    participants = db.relationship("Participant", backref="participant")