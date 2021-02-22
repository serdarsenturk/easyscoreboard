from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

#Define the database object which is imported
db = SQLAlchemy(app)

# Import a module / component using its blueprint handler variable (ex./url)
from app.api.scoreboard import url as api

#Register blueprint(s)
app.register_blueprint(api)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
