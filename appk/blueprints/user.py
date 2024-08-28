from flask import Blueprint, request

bp = Blueprint("user", __name__)


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
