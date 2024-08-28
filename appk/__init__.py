from flask import Flask, request

from app_copy.blueprints import web, user

app = Flask(__name__)  # is the file name

app.register_blueprint(web.bp)
app.register_blueprint(user.bp)
