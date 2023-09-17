#!/usr/bin/python3
"""A CLASS SQUARE THAT INHERITS FROM CLASS RECTANGLE"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square object that inherits
            from the Rectangle class.

    Attributes:
    ----------
    inherits all attributes of Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Gets the size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of a Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle object."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
