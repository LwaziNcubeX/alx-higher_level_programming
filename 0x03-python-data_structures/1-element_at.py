#!/usr/bin/python3
def element_at(my_list, idx):
    print(len(my_list))

    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    else:
        return idx + 1
