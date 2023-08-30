#!/usr/bin/python3
"""Print Square instance"""


class Square:
    """
    Represents a square with a given size and position.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)):
            Initializes a new square object.
        area(self):
            Calculates the area of the square.
        my_print(self):
            Prints the square to the console.
        __str__(self):
            Returns the string representation of the square.
        __repr__(self):
            Returns the string representation of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with a given size and position.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer,
                       or position is not a tuple of 2 positive integers.
            ValueError: If size or either element in position is negative.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method to return the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If either element of value is negative.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to the console using '#' character and position.

        If the size of the square is 0, an empty line is printed.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return self.__repr__()

    def __repr__(self):
        """
        Returns the string representation of the square.
        """
        s = "\n" * self.__position[1]
        x = self.__size + "\n"
        s += (" " * self.__position[0] + "#" * x) * self.__size
        return s[:-1]
