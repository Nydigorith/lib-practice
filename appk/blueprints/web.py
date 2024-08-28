from flask import Blueprint, request, render_template

bp = Blueprint("web", __name__)


@bp.route("/")  # decorator
def index():
    return "<h1>Hello, World!</h1>"


@bp.route("/about")
def about():  # function name doesn't matter
    return render_template("/about/index.html", id="1234")


# @web.route('/user/')
# def user():
#     return "<h1>All User</h1>"


@bp.route("/user", methods=["POST", "GET"])
def user():
    # return "<h1>Create User</h1>"
    if request.method == "POST":
        return "You are using POST"
    else:
        return "You are using GET"


@bp.route("/user/<int:id>", methods=["DELETE", "PUT"])
def userId(id):
    if request.method == "DELETE":
        return f"You are using DELETE with id: {id}"
    else:
        return f"You are using PUT with id: {id}"


@bp.route("/blog/<string:name>/<int:id>")
def blog(name, id):
    return f"Hello {name}, your id is: {id}"
