#!/usr/bin/python3
"""To JSON string"""
import json


def to_json_string(my_obj):
    """
    JSON representation of an object (string):

    :param my_obj:
    :return: JSON representation
    """
    data = json.dumps(my_obj)
    return data
