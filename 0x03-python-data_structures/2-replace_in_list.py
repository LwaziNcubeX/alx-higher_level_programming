#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        #   del my_list[idx]
        #   new_list = my_list.insert(my_list[idx - 1], element)
        my_list[idx] = element
        return my_list
