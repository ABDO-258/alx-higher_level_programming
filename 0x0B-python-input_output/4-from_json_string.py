#!/usr/bin/python3
""" modul that returns the object of a json representation """
import json


def from_json_string(my_str):
    """ function that returns the object of a json representation """
    return json.loads(my_str)
