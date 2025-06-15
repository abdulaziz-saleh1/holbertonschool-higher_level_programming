#!/usr/bin/env python3
"""A simple Flask API that passes test_04_flask.py."""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory users
users = []


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})


@app.route('/data', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request must be JSON"}), 400

    username = data.get("username")
    email = data.get("email")

    if not username:
        return jsonify({"error": "Username is required"}), 400
    if not email:
        return jsonify({"error": "Email is required"}), 400

    new_user = {"username": username, "email": email}
    users.append(new_user)
    return jsonify(new_user), 201


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    for user in users:
        if user["username"] == username:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.errorhandler(404)
def handle_404(error):
    return jsonify({"error": "User not found"}), 404


if __name__ == '__main__':
    app.run()
