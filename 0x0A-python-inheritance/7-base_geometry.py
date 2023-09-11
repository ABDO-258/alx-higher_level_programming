#!/usr/bin/python3
""" modul of empty class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """
    def area(self):
        """ method that raise an exeption """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validation of value as integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
