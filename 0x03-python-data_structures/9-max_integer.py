#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    max = my_list[0]
    for j in range(length):
        if (my_list[j] > max):
            max = my_list[j]        
    return max
