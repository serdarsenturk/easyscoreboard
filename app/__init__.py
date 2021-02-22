from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Define the WSGI application object
app = Flask(__name__)
ma = Marshmallow(app)

# Configurations
app.config.from_object('config')

#Define the database object which is imported
db = SQLAlchemy(app)

# Import a module / component using its blueprint handler variable (ex./url)
from app.api.scoreboard import scoreboard as api
from app.api.home import home

#Register blueprint(s)
app.register_blueprint(api)
app.register_blueprint(home)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
