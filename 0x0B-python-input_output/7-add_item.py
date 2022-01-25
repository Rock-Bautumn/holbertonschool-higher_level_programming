#!/usr/bin/python3
"""
This python script adds an item to a json file
"""


import sys

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

try:
    jsonobject = load('add_item.json')
except:
    jsonobject = []

save(jsonobject + sys.argv[1:], 'add_item.json')
