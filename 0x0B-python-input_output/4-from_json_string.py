#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """
    From json string to object

    :param my_str:
    :return:
    """
    data = json.loads(my_str)
    return data
