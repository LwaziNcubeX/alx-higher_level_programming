#!/usr/bin/python3
class LockedClass:
    """
    Define the __slots__ attribute to only 
    allow a single instance attribute
    """
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError(
                    "'LockedClass' object has no attribute '" + name + "'")
        super().__setattr__(name, value)
