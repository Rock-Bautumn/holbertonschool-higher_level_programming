#!/usr/bin/python3


def uniq_add(my_list=[]):
    sum = 0
    s_list = sorted(my_list)
    for x in range(len(my_list)):
        if x == 0 or s_list[x] != s_list[x-1]:
            sum += s_list[x]
    return sum
