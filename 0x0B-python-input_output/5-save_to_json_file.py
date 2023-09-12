#!/usr/bin/python3
"""save to Object"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that write an Obj to File

    :param my_obj:
    :param filename:
    :return:
    """
    with open(filename, 'w', encoding="utf-8") as f:
        obj = json.dumps(my_obj)
        f.write(obj)
        f.close()
