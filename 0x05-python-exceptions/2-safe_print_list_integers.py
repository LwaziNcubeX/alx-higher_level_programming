#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    count_elements = lambda i: sum(1 for _ in i)
    total = count_elements(my_list) - 1
    for i in range(x):
        try:
            if isinstance(my_list[i], int) and my_list[i] <= total:
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except Exception:
            raise
    print()
    return count
