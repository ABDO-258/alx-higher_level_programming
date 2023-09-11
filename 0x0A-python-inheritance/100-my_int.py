#!/usr/bin/python3
""" module  MyInt is a rebel """


class MyInt(int):
    """subclass MyInt has == and != operators inverted"""
    def __eq__(self, other):
        """ change == to != """
        return super().__ne__(other)

    def __ne__(self, other):
        """ change != to == """
        return super().__eq__(other)
