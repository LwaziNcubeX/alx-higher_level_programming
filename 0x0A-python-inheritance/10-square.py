#!/usr/bin/python3
""" Improve Geometry """


class BaseGeometry:
    """
    A class BaseGeometry (based on 6-base_geometry.py).

    :raise Exception, TypeError, ValueError
    :return Nothing
    """
    def area(self):
        raise Exception("area() is not implemented")

    @staticmethod
    def integer_validator(name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

    width: The width of the rectangle (must be a positive integer)
    height: The height of the rectangle (must be a positive integer)

    return: An instance of Rectangle
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        width: The width of the rectangle (must be a positive integer)
        height: The height of the rectangle (must be a positive integer)
        raises ValueError: If either width or
            height is not a positive integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.

    size: The size of the square (must be a positive integer)
    raises ValueError: If size is not a positive integer
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        return: The area of the square
        """

        return self.__size ** 2

    def __str__(self):
        """String Method"""

        return "[Rectangle] {}/{}".format(self.__size, self.__size)
