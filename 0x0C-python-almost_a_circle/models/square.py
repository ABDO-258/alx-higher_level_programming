#!/usr/bin/python3
""" modul rectangle """
# Rectangle = __import__('rectangle').Rectangle
from models.rectangle import Rectangle


class Square(Rectangle):
    """creat a square object"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialise the square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return the string representation of a Square"""
        return ("[{}] ({}) {}/{} - {}".format
                (self.__class__.__name__,
                 self.id, self.x, self.y,
                 self.width))

    @property
    def size(self):
        """ getting the size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """ setting the size of a square"""
        self.validate_int("width", value)
        self.validate_bigger_or_zero("width", value)
        self.width = value

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            list_args = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_args[i], args[i])
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """return the dictionary representation of a Square """
        list_args = ['id', 'x', 'size', 'y']
        dictionnary = {}
        for key in list_args:
            dictionnary[key] = getattr(self, key)
        return dictionnary
