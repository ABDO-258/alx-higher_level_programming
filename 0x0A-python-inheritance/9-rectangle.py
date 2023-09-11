#!/usr/bin/python3
""" modul  class Rectangle  """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle subclass of BaseGeometry """
    def __init__(self, width, height):
        """Intialize a Rectangle """
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[{}] {}/{}".format
                (self.__class__.__name__,
                 self.__width, self.__height))
