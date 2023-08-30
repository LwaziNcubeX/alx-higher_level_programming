#!/usr/bin/python3
"""magic class for a bytcode"""

import math


class MagicClass:
    """
    A class representing a magic circle.
    """

    def __init__(self, radius):
        """
        Initializes a MagicClass object with a given radius value.

        :radius: The radius of the circle.
        """
        self.__radius = radius

    def area(self):
        """
        Returns the area of the circle.

        :return: The area of the circle.
        """
        return (math.pi * self.__radius ** 2)

    def circumference(self):
        """
        Returns the circumference of the circle.

        :return: The circumference of the circle.
        """
        return (2 * math.pi * self.__radius)
