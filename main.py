from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:****@0.0.0.0:5432/easyscoreboard',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
db = SQLAlchemy(app)

#Note how we never defined a __init__ method on the ScoreBoard class?
#That’s because SQLAlchemy adds an implicit constructor to all 
#model classes which accepts keyword arguments for all its columns and relationships. 

class ScoreBoard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<ScoreBoard %r>' % self.name 

@app.route('/')
def homeView():
    return "<h1>Welcome to Easy Score Board.</h1>"

@app.route('/api/v1/hello', methods = ["GET"])
def readById():
    scoreboard = ScoreBoard.query.filter_by(id=1)
    return render_template("show_by_id.html", scoreboards=scoreboard)