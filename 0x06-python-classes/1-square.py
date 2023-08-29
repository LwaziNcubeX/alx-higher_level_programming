#!/usr/bin/python3
"""Square with size"""


class Square:
    """
    This class defines a square with a private instance attribute "size".

    Attributes:
        __size (int): The size of the square, which is
                      a private instance attribute.

    Methods:
        None.
    """
    def __init__(self, size):
        """
        This ia a constructor for the Square class.

        Args:
            size (int): The size of the square.

        """
        self.__size = size
