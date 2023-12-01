#!/usr/bin/python3
def find_peak(list_of_integers):
    """ find a peak """
    if len(list_of_integers) == 0:
        return None
    else:
        my_list = sorted(list_of_integers)
        return my_list[-1]