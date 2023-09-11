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
