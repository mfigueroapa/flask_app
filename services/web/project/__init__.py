from flask import Flask, jsonify


app = Flask(__name__)
app.config.from_object("project.config.Config")


@app.route("/")
def home():
    return jsonify(hello="world")

@app.route("/health")
def health():
    return jsonify(hello="upupup")