#!/usr/bin/python3
""" a class Student that defines a student by:
first_name
last_name
age """


class Student:
    """ a class Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary description with simple
        data structure (list, dictionary, string, integer and boolean)
        for JSON serialization of an object """
        if type(attrs) is list:
            if all(type(element) is str for element in attrs):
                return {key: self.__dict__[key]
                        for key in attrs if key in self.__dict__}
        return self.__dict__
