#!/usr/bin/python3
def infinit_add():
    import sys
    a = sys.argv[1:]
    total = 0

    for i in range(len(a)):
        total = total + int(a[i])
    print(total)


if __name__ == "__main__":
    infinit_add()
