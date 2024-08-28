from flask import Flask
from app.extensions import db
from app.blueprints import web, user


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
app.register_blueprint(web.bp)
app.register_blueprint(user.bp)


with app.app_context():
    db.create_all()
