#!/usr/bin/python3
"""module of a sub class Mylist"""


class Mylist(list):
    """ subclass Mylist """

    def print_sorted(self):
        """print the list in a sorted order"""
        print(sorted(self))
