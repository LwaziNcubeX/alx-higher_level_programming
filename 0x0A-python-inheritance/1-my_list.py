#!/usr/bin/python3
"""my list"""


class MyList(list):
    """
    A class MyList that inherits from list
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
