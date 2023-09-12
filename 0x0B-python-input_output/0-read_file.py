#!/usr/bin/python3
"""READ TEXT FILE(UTF8)"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8)
    and prints it to stdout

    :param filename:
    :return: Nothing
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
