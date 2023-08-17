#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    update_dict = dict(map(lambda x: (key, value) if x[0] == key else x, a_dictionary.items()))
    a_dictionary.update(update_dict)
    return a_dictionary
