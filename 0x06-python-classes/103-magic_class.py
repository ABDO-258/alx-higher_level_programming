#!/usr/bin/python3
"""define a MagicClass and it methodes """
import math


class MagicClass:
    """ MagicClass == circle"""
    def __init__(self, radius):
        '''initialize the MagicClass'''
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calcule area of MagicClass """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calcule circumference of MagicClass """
        return 2 * math.pi * self.__radius
