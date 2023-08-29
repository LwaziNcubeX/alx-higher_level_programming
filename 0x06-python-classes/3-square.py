#!/usr/bin/python3
"""Square with size validation"""


class Square:
    """
    This class defines a square with:
     - A private instance attribute "size".
     - Size validation
     - Area of a Square

    Attributes:
        __size (int): The size of the square, which is
                      a private instance attribute.
         area (self): A Public instance method that
                      returns area of a square.

    Methods:
        1. def __init__(self, size=0)
        2. def area(self)
    """
    def __init__(self, size=0):
        """
        This ia a constructor for the Square class.

        Args:
            size (int): The size of the square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of a square.

        Args:
            None, just self only
        """
        total = self.__size ** 2
        return total
