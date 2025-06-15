#!/usr/bin/env python3
"""A simple Flask API."""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data
users = [
    {"id": 1, "username": "alice", "email": "alice@example.com"},
    {"id": 2, "username": "bob", "email": "bob@example.com"}
]


@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Flask API!"})


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request must be JSON"}), 400

    username = data.get('username')
    email = data.get('email')

    if not username:
        return jsonify({"error": "Username is required"}), 400
    if not email:
        return jsonify({"error": "Email is required"}), 400

    new_user = {
        "id": len(users) + 1,
        "username": username,
        "email": email
    }
    users.append(new_user)
    return jsonify(new_user), 201


if __name__ == '__main__':
    app.run(debug=True)
