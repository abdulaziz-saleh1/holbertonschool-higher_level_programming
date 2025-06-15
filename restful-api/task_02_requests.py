#!/usr/bin/env python3
"""Script to fetch and process data from JSONPlaceholder API using Python."""

import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts from the API and print titles if successful."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetch all posts and save them as a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        # extract only id, title, and body
        filtered = [{'id': p['id'], 'title': p['title'], 'body': p['body']} for p in posts]

        with open("posts.csv", mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(filtered)
