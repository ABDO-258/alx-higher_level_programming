#!/usr/bin/python3
""" module that create a rectangle"""


class Rectangle:
    """ class that create a rectangle"""
    def __init__(self, width=0, height=0):
        """ intialize  a rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """ getting the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setting the width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getting the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ getting the height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
