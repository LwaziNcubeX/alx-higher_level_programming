#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """
    A function that writes string to text file

    :param filename:
    :param text:
    :return:
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        f.close()
    return len(text)
