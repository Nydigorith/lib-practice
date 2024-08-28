from app.models.user import User as UserModel

from flask import Blueprint, redirect, render_template, request, url_for
from app.extensions import db

bp = Blueprint("user", __name__)


@bp.route("/user/")
def index():

    users = UserModel.query.all()
    return render_template("user/index.html", users=users)
    # return "<h1>Get User!</h1>"


@bp.route("/user/", methods=["POST"])
def store():
    # store user in db
    newUser = UserModel(name=request.form["name"], email=request.form["email"])
    db.session.add(newUser)
    db.session.commit()

    return redirect(url_for("user.index"))


@bp.route("/user/create")
def create():
    return render_template("user/create.html")


@bp.route("/user/<int:id>", methods=["DELETE", "PUT"])
def user_id(id):
    if request.method == "DELETE":

        user = UserModel.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return "Deleted!"

    elif request.method == "PUT":
        return "<h1>Update User!</h1>"


@bp.route("/user/<int:id>")
def about(id):
    return render_template("user/show.html", id=id)
    return render_template("user/show.html", id=id)
