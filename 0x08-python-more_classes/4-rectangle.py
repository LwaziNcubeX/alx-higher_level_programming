#!/usr/bin/python3
"""Area and Perimeter"""


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

    def area(self):
        """
        calculates area of a rectangle

        Returns:
            area
        """
        return self.height * self.width

    def perimeter(self):
        """
        calculates perimeter of a rec
        Returns:
            0 if width or height = 0
            else:
                total perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.height + self.width) * 2

    def __str__(self):
        """
        prints the rectangle with the char #

        Returns:
            empty string if width or height = 0
            else:
                prints str #
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            output = []
            for i in range(self.height):
                output.append("#" * self.width)
            return "\n".join(output)

    def __repr__(self):
        """
        string representation of the object

        Returns:
            a string

        """
        return f"Rectangle({self.width}, {self.height})"
