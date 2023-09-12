#!/usr/bin/python3
""" module to append write to a text file"""


def append_write(filename="", text=""):
    """function to append write to a text file"""

    with open(filename, mode="a", encoding="utf-8") as Myfile:
        return Myfile.write(text)
