#!/usr/bin/python3
def common_elements(set_1, set_2):
    commonElements = set(filter(lambda x: x in set_1, set_2))
    return commonElements
