#!/usr/bin/python3
""" Can I?"""


def add_attribute(obj, name, value):
    """
    Add a new attribute to an object if it's possible.

    Args:
        obj: The object to add the attribute to
        name: The name of the attribute
        value: The value of the attribute
    :raises TypeError: If the object can't have new attributes
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
