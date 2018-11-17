#!/usr/bin/env python
from flask import Flask, render_template, Response, jsonify
# from camera import VideoCamera

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return "Hello World"


@app.route('/get', methods=["POST"])
def get():
    response_ = {
        "response": "Hello Hao"
    }
    return jsonify(response_)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)