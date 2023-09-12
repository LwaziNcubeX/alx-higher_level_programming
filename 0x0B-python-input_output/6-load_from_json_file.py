#!/usr/bin/python3
"""Create obj from JSON file"""
import json


def load_from_json_file(filename):
    """
    A function that creates object
    from json File

    :param filename:
    :return:
    """
    with open(filename, 'r') as f:
        obj = json.load(f)
        f.close()

    return obj
