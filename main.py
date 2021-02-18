from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:****@localhost:5432/easyscoreboard'
db = SQLAlchemy(app)

@app.route('/')
def homeView():
    return "<h1>Welcome to Easy Score Board.</h1>"

@app.route('/api/v1/hello', methods = ["GET"])
def printHello():
    return 'Hello, World'