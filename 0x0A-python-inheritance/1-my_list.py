#!/usr/bin/python3

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
        self.sort()
        print(self)
