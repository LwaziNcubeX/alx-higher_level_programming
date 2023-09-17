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
        return json.dumps(list_dictionaries)
