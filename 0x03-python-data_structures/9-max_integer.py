#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    max = 0
    for j in range(length):
        if (max > my_list[j]):
            max = max
        else:
            max = my_list[j]
    return max
