from flask import Flask, request

app = Flask(__name__)  # is the file name


@app.route("/")  # decorator
def index():
    return "<h1>Hello, World!</h1>"


@app.route("/about")
def about():  # function name doesn't matter
    return "<h1>About Page</h1>"


# @app.route('/user/')
# def user():
#     return "<h1>All User</h1>"


@app.route("/user", methods=["POST", "GET"])
def user():
    # return "<h1>Create User</h1>"
    if request.method == "POST":
        return "You are using POST"
    else:
        return "You are using GET"


@app.route("/user/<int:id>", methods=["DELETE", "PUT"])
def userId(id):
    if request.method == "DELETE":
        return f"You are using DELETE with id: {id}"
    else:
        return f"You are using PUT with id: {id}"


@app.route("/blog/<string:name>/<int:id>")
def blog(name, id):
    return f"Hello {name}, your id is: {id}"
