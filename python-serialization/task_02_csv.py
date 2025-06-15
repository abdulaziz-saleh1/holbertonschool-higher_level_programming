#!/usr/bin/python3
"""Module for converting CSV data to JSON format using serialization."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to a JSON file (data.json).
    Returns True if successful, False if file not found or other errors occur.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
