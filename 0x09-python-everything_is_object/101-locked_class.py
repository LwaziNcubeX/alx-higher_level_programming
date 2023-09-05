#!/usr/bin/python3
""" LOCKED CLASS """


class LockedClass:
    """A class that only allows a single, pre-defined attribute."""

    __slots__ = ['first_name']
    """The __slots__ attribute is used to optimize memory usage.
    This class has only one allowed attribute, 'first_name'."""

    def __setattr__(self, name, value):
        """Override the __setattr__ method to prevent dynamic creation
        of attributes except for the allowed 'first_name' attribute."""

        if not hasattr(self, name) and name != 'first_name':
            """Check if the attribute being set is not already defined
            and is not the allowed 'first_name' attribute."""

            raise AttributeError(
                    "'LockedClass' object has no attribute '" + name + "'")

        super().__setattr__(name, value)
        """Set the attribute and its value using the parent class's
        implementation of __setattr__."""
