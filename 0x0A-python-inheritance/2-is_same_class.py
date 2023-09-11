#!/usr/bin/python3
""" module to check if an object is an instance of class"""


def is_same_class(obj, a_class):
    """ function that returns True if the object is
        exactly an instance of the specified class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
