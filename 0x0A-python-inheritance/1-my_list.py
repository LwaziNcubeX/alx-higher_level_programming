#!/usr/bin/python3
"""my list"""


class MyList(list):
    """
    A class that inherits from list and provides additional functionality.
    """

    def __init__(self):
        """
        Initializes a new instance of the MyList class.
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        self.sort()
        print(self)
