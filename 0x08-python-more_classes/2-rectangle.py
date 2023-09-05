#!/usr/bin/python3
""" module that create a rectangle"""


class Rectangle:
    """ class that create a rectangle"""
    def __init__(self, width=0, height=0):
        """ intialize  a rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getting the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setting the width of a rectangle"""
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """ methode that return tha area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ methode that return tha perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((2 * self.__width) + (2 * self.__height))
