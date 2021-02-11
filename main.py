from flask import Flask

app = Flask(__name__)

@app.route('/')
def homeView():
    return "<h1>Welcome to easyscoreboard.</h1>"

@app.route('/api/v1/hello', methods = ["GET"])
def printHello():
    return 'Hello, World'