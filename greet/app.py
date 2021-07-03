from flask import Flask, request

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "welcome"


@app.route("/welcome/home")
def welcome_home():
    return "welcome_home"

@app.route("/welcome/back")
def welcome_back():
    return "welcome back"


