#!/usr/bin/python3
"""BASE CLASS"""
import json


class Base:
    """
    Represents the base class that manages the id
        attribute in all other classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance with a unique id.

        id: An optional integer id to initialize the Base instance with.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation"""
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))
