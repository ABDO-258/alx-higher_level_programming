#!/usr/bin/python3
""" modul  script that adds all arguments to a Python list,
and then save them to a file """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    list_of_args = load_from_json_file("add_item.json")
except FileNotFoundError:
    list_of_args = []
list_of_args.extend(sys.argv[1:])
save_to_json_file(list_of_args, "add_item.json")
