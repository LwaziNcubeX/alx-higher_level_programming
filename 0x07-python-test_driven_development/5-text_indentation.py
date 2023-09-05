#!/usr/bin/python3
""" TEXT INDENTATION """


def text_indentation(text):
    """
    A function prints a text with 2 new lines
        after each of these characters.

    Args:
        text
    Return:
        None
    Raises:
        None
    """
    if isinstance(text, str):
        new_text = ""
        for char in text:
            new_text += char
            if char in [".", "?", ":"]:
                new_text += "\n\n"
        lines = new_text.split("\n")
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
        print("\n".join(lines))
    elif not isinstance(text, str):
        raise TypeError("text must be a string")
