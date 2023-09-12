#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a text file (UTF8)

    :param filename:
    :param text:
    :return: the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        f.close()
    return len(text)
