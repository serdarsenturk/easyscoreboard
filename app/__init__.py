from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from config import Config

#Define the WSGI application object
app = Flask(__name__)
ma = Marshmallow(app)

# Configurations
app.config.from_object(Config)
#Define the database object which is imported
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import a module / component using its blueprint handler variable (ex./url)
from app.api.board import boards as board_api
from app.api.participant import participants as participants_api
from app.api.score import scores as scores_api
from app.api.home import home

#Register blueprint(s)
app.register_blueprint(board_api)
app.register_blueprint(participants_api)
app.register_blueprint(scores_api)
app.register_blueprint(home)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
