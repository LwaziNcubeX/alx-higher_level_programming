#!/usr/bin/python3
""" SAY MY NAME """


def say_my_name(first_name, last_name=""):
    """
    A function that prints my name & last name

    Args:
        first_name - string
        last_name - string
    Returns:
        Nothing
    Raises:
        TypeError - if one or both args are not str
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print(f"My name is {first_name} {last_name}")
    elif not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
