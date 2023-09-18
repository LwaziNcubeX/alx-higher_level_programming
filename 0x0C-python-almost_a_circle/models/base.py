#!/usr/bin/python3
"""BASE CLASS"""
import csv
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
        if not list_dictionaries:
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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == "Rectangle":
            dummy = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            dummy = Square(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """A class method that returns a list of instances:"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                json_list = cls.from_json_string(f.read())
                return [cls.create(**d) for d in json_list]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances of the class loaded from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                objs = []
                for row in reader:
                    data_dict = {}
                    if cls.__name__ == "Rectangle":
                        attrs = ("id", "width", "height", "x", "y")
                    elif cls.__name__ == "Square":
                        attrs = ("id", "size", "x", "y")
                    for i, attr in enumerate(attrs):
                        data_dict[attr] = int(row[i])
                    obj = cls.create(**data_dict)
                    objs.append(obj)
                return objs
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of instances of the class to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            csv_writer = csv.writer(f)
            for obj in list_objs:
                row = [getattr(obj, a) for a in obj.__dict__.keys()]
                csv_writer.writerow(row)
