from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)

@app.route("/add")
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a,b))


@app.route("/sub")
def do_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a,b))

@app.route("/mult")
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a,b))

@app.route("/div")
def do_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a,b))

operations = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<operation>")
def do_all_in_one(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operations[operation](a, b))
