# hello.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Docker!"

app.run("0.0.0.0")
