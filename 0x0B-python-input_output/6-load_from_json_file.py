#!/usr/bin/python3
""" modul  that creates an Object from a “JSON file """
import json


def load_from_json_file(filename):
    """ function function that creates an Object from a “JSON file"""
    with open(filename, mode="r") as Myfile:
        return json.load(Myfile)
