#!/usr/bin/python3
""" modul rectangle """
# Base = __import__('base').Base
from models.base import Base


class Rectangle(Base):
    """creat a rectangle object"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialise the rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def validate_int(self, arg, value):
        """ validate input value is int """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(arg))

    def validate_bigger_or_zero(self, arg, value):
        """ validate input value is > 0 """
        if value <= 0:
            raise ValueError("{} must be > 0".format(arg))

    def validate_bigger_than_zero(self, arg, value):
        """ validate input value is not negative """
        if value < 0:
            raise ValueError("{} must be >= 0".format(arg))

    @property
    def width(self):
        """ getting the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setting the width of a rectangle"""
        self.validate_int("width", value)
        self.validate_bigger_or_zero("width", value)
        self.__width = value

    @property
    def height(self):
        """ getting the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setting the height of a rectangle"""
        self.validate_int("height", value)
        self.validate_bigger_or_zero("height", value)
        self.__height = value

    @property
    def x(self):
        """ getting x of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setting the x of a rectangle"""
        self.validate_int("x", value)
        self.validate_bigger_than_zero("x", value)
        self.__x = value

    @property
    def y(self):
        """ getting y of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setting the y of a rectangle"""
        self.validate_int("y", value)
        self.validate_bigger_than_zero("y", value)
        self.__y = value

    def area(self):
        """ the area of a Rectangle """
        return self.__height * self.__width

    def display(self):
        """ that prints in stdout the Rectangle
          instance with the character # """
        string = ""
        if self.__width == 0 or self.__height == 0:
            print(string)
        else:
            for _ in range(self.__y):
                string += "\n"

            for i in range(self.__height):
                for _ in range(self.__x):
                    string += " "
                if i == (self.__height - 1):
                    string += ("#" * self.__width)
                else:
                    string += (("#" * self.__width) + "\n")
        print(string)

    def __str__(self):
        """ reurn a string reprisantation of a rectangle"""
        return ("[{}] ({}) {}/{} - {}/{}".format
                (self.__class__.__name__,
                 self.id, self.__x, self.__y,
                 self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ update a rectangle"""
        if args is not None and len(args) != 0:
            list_args = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_args[i], args[i])
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """ return the dictionary representation of a Rectangle"""
        list_args = ['x', 'y', 'id', 'height', 'width']
        dictionnary = {}
        for key in list_args:
            dictionnary[key] = getattr(self, key)
        return dictionnary
