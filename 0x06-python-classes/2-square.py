#!/usr/bin/python3
''' Squre class to make a square '''


class Square:
    ''' create an empty class'''
    def __init__(self, size=0):
        '''
        intialize the class

        size = size of a square
        size must be an integer
        size must be bigger than 0

        '''

        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
