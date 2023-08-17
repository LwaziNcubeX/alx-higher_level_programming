#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multi2 = dict(map(lambda elem: (elem[0], elem[1]*2), a_dictionary.items()))
    return multi2
