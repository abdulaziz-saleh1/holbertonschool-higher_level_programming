#!/usr/bin/python3
"""Script that adds all arguments to a Python list,
and then saves them to a file.
"""


import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

if exists(filename):
    try:
        my_list = load_from_json_file(filename)
    except Exception:
        my_list = []
else:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
