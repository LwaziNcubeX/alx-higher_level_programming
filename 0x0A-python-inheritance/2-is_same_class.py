#!/usr/bin/python3
""" Exact same object """


def is_same_class(obj, a_class):
    """
    Exact same object [FUNCTION]
    Args:
        obj
        a_class

    return:
        True - if the object is exactly an instance of
                the specified class
        False - otherwise
    """
    a = type(obj)
    return a == a_class
