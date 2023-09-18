#!/usr/bin/python3
""" something """
import json
import csv


class Base:
    """ a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialise the Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ staticmethod that return the JSON string representation
         of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ that writes the JSON string
         representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        list_instance = []

        if list_objs is not None and len(list_objs) > 0:
            for instance in list_objs:
                list_instance.append(instance.to_dictionary())
        with open(filename, mode="w") as myfile:
            myfile.write(cls.to_json_string(list_instance))

    @staticmethod
    def from_json_string(json_string):
        """ that returns the list of the JSON string representation """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        elif cls.__name__ == "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ method that returns a list of instances"""
        filename = cls.__name__ + ".json"
        list_of_cls = []
        try:
            with open(filename, mode="r") as myfile:
                for element in cls.from_json_string(myfile.read()):
                    list_of_cls.append(cls.create(**element))
                return list_of_cls
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ that serializes and deserializes in CSV file """
        filename = cls.__name__ + ".csv"
        rows_data = []
        for object in list_objs:
            if cls.__name__ == "Rectangle":
                header = ["width", "height", "x", "y", "id"]
                data = [object.width, object.height,
                        object.x, object.y, object.id]
            elif cls.__name__ == "Square":
                header = ["size", "x", "y", "id"]
                data = [object.size, object.x, object.y, object.id]
            rows_data.append(data)
        with open(filename, mode="w") as myfile:
            writing = csv.writer(myfile)
            # the header
            writing.writerow(header)
            # object data
            writing.writerows(rows_data)

    @classmethod
    def load_from_file_csv(cls):
        """ method that returns a list of instances"""
        filename = cls.__name__ + ".csv"
        list_of_cls = []
        try:
            with open(filename, mode="r") as myfile:
                reader = csv.reader(myfile)

                header = next(reader)

                for row in reader:
                    if cls.__name__ == "Rectangle":
                        # Create a Rectangle instance from the CSV data
                        width, height, x, y, obj_id = map(int, row)
                        instance = cls(width=width, height=height,
                                       x=x, y=y, id=obj_id)
                    elif cls.__name__ == "Square":
                        # Create a Square instance from the CSV data
                        size, x, y, obj_id = map(int, row)
                        instance = cls(size=size, x=x, y=y, id=obj_id)
                    list_of_cls.append(instance)
                return list_of_cls
        except FileNotFoundError:
            return []
