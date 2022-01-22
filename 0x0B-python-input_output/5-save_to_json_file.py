#!/usr/bin/python3
"""
this module contains a function to save an object to a json file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    saves object to json file
    """

    with open(filename, "w") as jsonfile:
        jsonfile.write(json.dumps(my_obj))
