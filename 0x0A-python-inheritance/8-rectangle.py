#!/usr/bin/python3
""" modul  class Rectangle  """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle subclass of BaseGeometry """
    def __init__(self, width, height):
        """Intialize a Rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
