#!/usr/bin/python3
""" MATRIX DIVISION """


def matrix_divided(matrix, div):
    """
    A function that divides the elements of a matrix

    Args:
        matrix - a matrix (list of lists) of integers/floats
        div - a number (integer or float)
    Returns:
        new_matrix - with the elements divided by div and
                        rounded to 2 decimal places
    Raises:
        TypeError - if the matrix is not a list of lists of integers/floats,
                        or if div is not a number
        ZeroDivisionError - if div is zero
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) and all(
                isinstance(elem, (int, float)) for elem in row
                ) for row in matrix
            ):
        error = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(error)
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = list(map(lambda row: list(
            map(lambda x: round(x / div, 2), row)), matrix))
        return new_matrix
