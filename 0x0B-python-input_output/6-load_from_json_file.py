#!/usr/bin/python3
"""
this module contains a function to create an object from a json file
"""


import json


def load_from_json_file(filename):
    """
    this creates an object from a json file
    """

    with open(filename) as jsonfile:
        return json.load(jsonfile)
