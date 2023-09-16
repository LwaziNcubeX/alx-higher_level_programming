#!/usr/bin/python3
"""implement __str__"""
from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle object that inherits from the Base class.

    Attributes:
    ----------
    __width : int
        the width of the rectangle
    __height: int
        the height of the rectangle
    __x : int
        the horizontal position of the rectangle
    __y : int
        the vertical position of the rectangle
    id : int
        the id of the rectangle object
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        :param width:
        :param height:
        :param x:
        :param y:
        :param id:
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def validate_integer(value, name):
        """check if value is int or not"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

    @staticmethod
    def validate_gt_zero(value, name):
        """check if value is less than or equal to zero"""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def validate_ge_zero(value, name):
        """check if value is less than zero"""
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        :return:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        :param value:
        :return:
        """
        self.validate_integer(value, "width")
        self.validate_gt_zero(value, "width")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        :return:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        :param value:
        :return:
        """
        self.validate_integer(value, "height")
        self.validate_gt_zero(value, "height")
        self.__height = value

    @property
    def x(self):
        """
        Gets the horizontal position of the rectangle.
        :return:
            The horizontal position of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the horizontal position of the rectangle.
        :param value:
        :return:
        """
        self.validate_integer(value, "x")
        self.validate_ge_zero(value, "x")
        self.__x = value

    @property
    def y(self):
        """
        Gets the vertical position of the rectangle.

        :return:
            The vertical position of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the vertical position of the rectangle.
        :param value:
        :return:
        """
        self.validate_integer(value, "y")
        self.validate_ge_zero(value, "y")
        self.__y = value

    def area(self):
        """
        Calculate Area

        :return:
            the area value of the Rectangle instance
        """
        return self.__width * self.height

    def display(self):
        """display a Rectangle using the # char"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
