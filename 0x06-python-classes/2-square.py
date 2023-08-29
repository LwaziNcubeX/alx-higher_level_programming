#!/usr/bin/python3
"""Square with size validation"""


class Square:
    """
    This class defines a square with a private instance attribute "size".
    Size validation added

    Attributes:
        __size (int): The size of the square, which is
                      a private instance attribute.

    Methods:
        def __init__(self, size=0)
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
