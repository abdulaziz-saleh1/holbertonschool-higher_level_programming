#!/usr/bin/env python3
"""Flask API exactly matching the expected output."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Store users as a dictionary with usernames as keys
users = {}


@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Flask API!"})


@app.route('/status', methods=['GET'])
def status():
    return "OK", 200


@app.route('/data', methods=['GET'])
def list_usernames():
    return jsonify(list(users.keys()))


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    username = data.get('username')
    name = data.ge
