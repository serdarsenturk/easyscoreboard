from flask import Flask

app = Flask(__name__)

print("Hello World")

@app.route('/api/v1/hello', methods = ["GET"])
def printHello():
    return 'Hello, World'