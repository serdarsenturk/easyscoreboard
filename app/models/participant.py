from .. import db

class Participant(db.Model):
    __tablename__ = 'participants'
    __table_args__ = (
        db.UniqueConstraint('board_id', 'name', name='unq_board_id_name'),
    )

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.VARCHAR(25), nullable=False)
    code = db.Column(db.String(8), nullable=False, unique=True, index=True)
    board_id = db.Column(db.Integer, db.ForeignKey('boards.id'), nullable=False)
    score = db.Column(db.Integer, server_default='0')