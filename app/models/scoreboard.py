#Note how we never defined a __init__ method on the ScoreBoard class?
#That’s because SQLAlchemy adds an implicit constructor to all
#model classes which accepts keyword arguments for all its columns and relationships.

from app import db

class ScoreBoard(db.Model):
    __tablename__ = 'score_boards'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    name = db.Column(db.String(80), unique=True, nullable=False)