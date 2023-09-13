#!/usr/bin/python3
""" modul of a function that returns True if the object is an instance
      of a class that inherited (directly or indirectly) from the specified
        class ; otherwise False.
    """


def inherits_from(obj, a_class):
    """ function that check the inheritance is derict or inderict """
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    return False
