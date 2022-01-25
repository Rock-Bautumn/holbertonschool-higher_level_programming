#!/usr/bin/python3
"""
This module contains a method to create an object from json
"""


import json


def from_json_string(my_str):
    """
    This returns an object from json
    """

    return json.loads(my_str)
