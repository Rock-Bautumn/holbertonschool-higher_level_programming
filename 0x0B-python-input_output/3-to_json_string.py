#!/usr/bin/python3
"""
This module contains function to jsonify a string
"""


import json


def to_json_string(my_obj):
    """
    This returns the jsonified version of the object
    """

    return json.dumps(my_obj)
