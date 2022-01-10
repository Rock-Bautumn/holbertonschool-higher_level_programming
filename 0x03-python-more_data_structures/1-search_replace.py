#!/usr/bin/python3


def search_replace(my_list, search, replace):
    edit_list = []
    for n in range(len(my_list)):
        if my_list[n] == search:
            edit_list.append(replace)
        else:
            edit_list.append(my_list[n])
    return edit_list
