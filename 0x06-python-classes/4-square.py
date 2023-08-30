#!/usr/bin/python3
"""Access and update private attribute"""


class Square:
    """
    This class defines a square with
      - a private instance attribute "__size"
      - public methods to get
      - set the size and calculate area.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes the square with a given size.
        area(self): Calculates the area of the square.
        size(self): Getter method to return the size of the square.
        size(self, value): Setter method to set the size of the square.
        __repr__(self): Returns a string representation of the Square object.
    """
    def __init__(self, size=0):
        """
        Initializes the Square object.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to return the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __repr__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A string representation of the Square object.
        """
        return f'Square({self.__size})'
