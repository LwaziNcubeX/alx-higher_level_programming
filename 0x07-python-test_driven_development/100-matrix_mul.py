#!/usr/bin/python3
"""MATRIX MUL"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices and return the result.

    Args:
        m_a (list): A matrix represented as a list of lists of integers or floats.
        m_b (list): A matrix represented as a list of lists of integers or floats.

    Returns:
        list: The product of the two input matrices.

    Raises:
        TypeError: If either of the input matrices is not a list,
                    not a list of lists, or contains elements other than integers or floats,
                    or the rows in the input matrices are not of the same size.
        ValueError: If either of the input matrices is empty,
                    or if the input matrices cannot be multiplied.

    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(val, (int, float)) for row in m_a for val in row) or not all(isinstance(val, (int, float)) for row in m_b for val in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # create result matrix
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # multiply matrices
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
