#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    commonElements = set(filter(lambda x: x in set_1, set_2))
    merge_set = set_1 | set_2
    diff_elements = set(filter(lambda x: x not in commonElements, merge_set))
    return diff_elements
