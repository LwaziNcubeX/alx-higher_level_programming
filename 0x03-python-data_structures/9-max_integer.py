#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max_value = 0
        for x in my_list:
            if x > max_value:
                max_value = x
            elif x < max_value:
                continue
        return max_value
