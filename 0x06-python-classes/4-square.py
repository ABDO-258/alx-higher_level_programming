#!/usr/bin/python3
''' Squre class to make a square '''


class Square:
    ''' a class  square that have size and methode area  '''

    def __init__(self, size=0):
        '''
        intialize the class

        size = size of a square
        size must be an integer
        size must be bigger than 0

        '''
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ methode to calculate the area of a square"""
        return self.__size * self.__size
