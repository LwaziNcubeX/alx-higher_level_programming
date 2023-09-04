#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """
    An empty class that defines a Rectangle

    Args:
        0

    Modules:
        None
    """
    def __init__(self, width=0, height=0):
        """
        Instantiates an object of this class

        Args:
            width (int, optional): Defaults to 0 if not provided.
            height (int, optional): Defaults to 0 if not provided.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Private instance attribute: width
        #READ ONLY

        Returns:
            self._width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Assigns a new variable for width
        that can be changed
        Args:
            value:

        Returns:
            Nothing
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """
        Private instance attribute: width
        #READ ONLY

        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Assigns a new variable for height
        that can be changed

        Args:
            value:

        Returns:
            Nothing
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
