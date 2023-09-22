#!/usr/bin/python3
"""BASE CLASS"""
import csv
import json
import random
import turtle


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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

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
    def save_to_file_csv(cls, list_objs):
        """save to file csv class method"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width,
                                     obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

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

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all Rectangles and Squares using Turtle graphics."""
        t = turtle.Turtle()
        t.speed(6)

        for rectangle in list_rectangles:
            # set a random fill color
            t.fillcolor(random.random(), random.random(), random.random())

            # draw the rectangle and save its position
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            t.begin_fill()
            t.pensize(3)
            for i in range(3):
                t.forward(rectangle.width)
                t.left(-90)
                t.forward(rectangle.height)
                t.left(-90)
            t.end_fill()

        for square in list_squares:
            t.fillcolor(random.random(), random.random(), random.random())

            # draw the square and save its position
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.color("blue", "red")
            t.pensize(3)
            for i in range(4):
                t.forward(square.size)
                t.right(-90)
            t.end_fill()

        turtle.mainloop()
