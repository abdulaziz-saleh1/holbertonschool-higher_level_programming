#!/usr/bin/env python3
"""Flask API that meets all exercise requirements exactly."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory dictionary to store users
users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


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
    username = data.get("username")
    name = data.get("name")
    age = data.get("age")
    city = data.get("city")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = {
        "username": username,
        "name": name,
        "age": age,
        "city": city
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
