def big_diff(my_list=[]):
    if len(my_list) <= 1:
        return 0
    min = my_list[0]
    max = my_list[0]
    for n in my_list:
        if n > max:
            max = n
        if n < min:
            min = n
    return max - min
