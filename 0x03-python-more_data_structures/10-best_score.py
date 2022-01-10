#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
#    print("dictionary has {:d} items".format(len(a_dictionary.values())))
    max = None
    for key, value in a_dictionary.items():
        if max is None or max < value:
            best = key
            max = value
    return best
