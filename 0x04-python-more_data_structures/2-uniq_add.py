#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set(filter(lambda x: my_list.count(x) == 1, my_list))
    non_unique = set(filter(lambda x: my_list.count(x) > 1, my_list))
    merged_set = unique_integers | non_unique
    total = 0
    for x in merged_set:
        total += x
    return total
