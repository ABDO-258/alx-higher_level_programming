#!/usr/bin/python3
""" module  class squre  """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square subclass of Rectangle """
    def __init__(self, size):
        """Intialize a Square """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
