#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """
    dictionary description with simple data structure

    :param obj:
    :return:
    """
    j = __import__('json')
    attributes = {}
    for attr in dir(obj):
        if not callable(getattr(obj, attr)) and not attr.startswith("__"):
            value = getattr(obj, attr)
            if isinstance(value, (list, dict, str, int, bool)):
                attributes[attr] = value
    return j.dumps(attributes)
