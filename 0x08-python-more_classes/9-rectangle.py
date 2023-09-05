#!/usr/bin/python3
""" A square is a rectangle """


class Rectangle:
    """
    An empty class that defines a Rectangle

    Args:
        0

    Modules:
        None
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Instantiates an object of this class

        Args:
            width (int, optional): Defaults to 0 if not provided.
            height (int, optional): Defaults to 0 if not provided.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
                output.append(str(self.print_symbol) * self.width)
            return "\n".join(output)

    def __repr__(self):
        """
        string representation of the object

        Returns:
            a string

        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        check which rect area is bigger
        Args:
            rect_1:
            rect_2:

        Returns:
            rect 1 if both rectangles are equal
            rect 2 if rect 1 is small
            rect 1 if rect 2 is small

        Raises:
            TypeErrors
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        A class method square
        Args:
            size:

        Returns:
            a new Rectangle instance
        """
        return Rectangle(size, size)
