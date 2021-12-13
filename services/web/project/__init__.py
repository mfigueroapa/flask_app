from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)
api = Api(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.route("/")
def home():
    return jsonify(data="world")

@app.route("/health")
def health():
    return jsonify(hello="server up")


# from project.routes import create_routes

# create_routes(api)

