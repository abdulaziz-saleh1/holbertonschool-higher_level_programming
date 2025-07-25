#!/usr/bin/python3
"""Script that adds all arguments to a Python list,
and then saves them to a file as JSON.
"""


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    try:
        my_list = load_from_json_file(filename)
    except Exception:
        my_list = []
else:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
