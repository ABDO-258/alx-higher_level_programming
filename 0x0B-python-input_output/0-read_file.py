#!/usr/bin/python3
""" module to read a text file"""


def read_file(filename=""):
    """function to read a text file"""

    with open(filename, encoding="utf-8") as Myfile:
        print(Myfile.read(), end="")
