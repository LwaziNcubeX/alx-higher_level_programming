#!/usr/bin/python3
""" Printing a square"""


class Square:
    """
    Represents a square with a given size.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new square object.
        size(self): Getter method to return the size of the square.
        size(self, value): Setter method to set the size of the square.
        area(self): Calculates the area of the square.
        my_print(self): Prints the square to the console.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square. Defaults to 0.

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

    def my_print(self):
        """
        Prints the square to the console using '#' character.

        If the size of the square is 0, an empty line is printed.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
