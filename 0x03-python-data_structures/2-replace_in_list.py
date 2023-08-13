#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx <= (len(my_list)):
        del my_list[idx]
        new_list = my_list.insert(my_list[idx - 1], element)
#        my_list[idx] = element
        return my_list
