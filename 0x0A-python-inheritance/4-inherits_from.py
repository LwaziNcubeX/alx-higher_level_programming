#!/usr/bin/python3
""" Only sub class of """


def inherits_from(obj, a_class):
    """
    if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj:
        a_class:

    return: True or false
    """
    a = type(obj)
    if a == a_class:
        return False
    else:
        return True
