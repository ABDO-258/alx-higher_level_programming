#!/usr/bin/python3
""" module to write to a text file"""


def write_file(filename="", text=""):
    """function to write to a text file"""

    with open(filename, mode="w", encoding="utf-8") as Myfile:
        return Myfile.write(text)
