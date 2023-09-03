#!/usr/bin/python3
"""PRINT SQUARE"""


def print_row(size):
    """
    A function that prints row

    Args: size
    """
    print("#" * size)


def print_square(size):
    """
    A funtion that prints a Square

    Args:
        size - the size length of the square
    Returns:
        Nothing
    Raises:
        TypeError:
        ValueError:
    """
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            for i in range(size):
                print_row(size)
    elif isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
