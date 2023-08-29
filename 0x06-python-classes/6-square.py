#!/usr/bin/python3
''' Squre class to make a square '''


class Square:
    ''' a class  square that have size and methode area and print  '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        intialize the class

        size = size of a square
        size must be an integer
        size must be bigger than 0

        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not  tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ methode to calculate the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """ methode to print the square"""
        if self.__position[1] > 0:
            print()

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print()
