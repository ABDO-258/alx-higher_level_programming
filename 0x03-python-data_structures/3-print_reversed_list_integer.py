#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        i = len(my_list)
        # print(i)
        while i != 0:
            print("{:d}".format(my_list[i-1]))
            i -= 1
