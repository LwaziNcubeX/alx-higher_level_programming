#!/usr/bin/python3
""" MyInt is a rebel """


class MyInt(int):
    """
    A class MyInt that inherits from int.

    The == and != operators are inverted.
    """

    def __eq__(self, other):
        """
        Invert the behavior of the == operator.
        """

        return int(self) != other

    def __ne__(self, other):
        """
        Invert the behavior of the != operator.
        """

        return int(self) == other
