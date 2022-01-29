#!/usr/bin/python3
"""
This module has the class Base
"""


import json


class Base:
    """
    This class is a base for geometrical shapes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Turns list of dictionaries into JSON string
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves JSON string to file
        """
        with open(cls.__name__ + ".json", 'w') as jsonfile:
            emptylist = []
            if list_objs is not None and len(list_objs) > 0:
                for i in list_objs:
                    emptylist.append(i.to_dictionary())
            jsonfile.write(cls.to_json_string(emptylist))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the json string representation
        """
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates and returns an object instance defined by **dictionary kwargs
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of object instances created from
        json file <class>.json
        """
        jsonfilename = cls.__name__ + ".json"
        try:
            with open(jsonfilename, "r") as jsonfile:
                jsonlist = cls.from_json_string(jsonfile.read())
            objectlist = []
            for object in jsonlist:
                objectlist.append(cls.create(**object))
            return objectlist
        except:
            return []


def validate_int(value, num):
    """
    validate that num is an integer,
    value is a string of what the num is, eg width
    """
    if type(value) is not str:
        raise TypeError("value passed to validate_int must be string")
    if type(num) is not int:
        raise TypeError(f"{value} must be an integer")
    if num <= 0:
        raise ValueError(f"{value} must be > 0")


def validate_not_neg(value, num):
    """
    validate that num is a 0 or positive integer,
    value is a string of what the num is, eg width
    """
    if type(value) is not str:
        raise TypeError("value passed to validate_not_neg must be string")
    if type(num) is not int:
        raise TypeError(f"{value} must be an integer")
    if num < 0:
        raise ValueError(f"{value} must be >= 0")
