#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for x, y in new_dict.items():
        update_dictionary(new_dict, x, y*2)
    return new_dict
