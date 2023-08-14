#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for x in my_list:
        if x % 2 == 0:
            new_list.append(True)
        elif x % 2 == 1:
            new_list.append(False)
    return new_list
