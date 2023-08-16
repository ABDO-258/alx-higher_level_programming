#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dictionary = sorted(a_dictionary.items())
    for key, value in new_dictionary:
        print(f"{key}:{value}")
