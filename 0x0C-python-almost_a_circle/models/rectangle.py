#!/usr/bin/python3
"""First Rectangle"""
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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        :return:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets the width of the rectangle.

        :param width:
        :return:
        """
        self.__width = width

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        :return:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the height of the rectangle.

        :param height:
        :return:
        """
        self.__height = height

    @property
    def x(self):
        """
        Gets the horizontal position of the rectangle.
        :return:
            The horizontal position of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Sets the horizontal position of the rectangle.
        :param x:
        :return:
        """
        self.__x = x

    @property
    def y(self):
        """
        Gets the vertical position of the rectangle.

        :return:
            The vertical position of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Sets the vertical position of the rectangle.
        :param y:
        :return:
        """
        self.__y = y
