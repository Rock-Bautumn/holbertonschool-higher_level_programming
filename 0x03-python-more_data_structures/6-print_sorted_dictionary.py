#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    s_dict = sorted(a_dictionary)
    for item in s_dict:
        print("{}: {}".format(item, a_dictionary[item]))
