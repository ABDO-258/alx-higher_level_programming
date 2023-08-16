#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_unique = list(set(my_list))
    result = 0
    for num in list_unique:
        result += num
    return result
