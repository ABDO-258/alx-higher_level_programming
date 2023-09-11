#!/usr/bin/python3
""" module to check if an object is an instance of class
or if the object is an instance of a class that inherited
from the specified class
"""


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is
         an instance or inheritance of the specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
