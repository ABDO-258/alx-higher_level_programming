#!/usr/bin/python3
""" modul  that creates an Object from a “JSON file """
import json


def save_to_json_file(my_obj, filename):
    """ function function that creates an Object from a “JSON file"""
    with open(filename, mode="r") as Myfile:
        return json.load(Myfile)
