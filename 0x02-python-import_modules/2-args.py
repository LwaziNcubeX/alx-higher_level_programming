#!/usr/bin/python3
def print_args():
    import sys
    argv = sys.argv[1:]
    n = len(argv)
    numList = []

    if n == 0:
        print("{} arguments.".format(n))
    else:
        print("{} arguments:".format(n))

    n = len(argv) + 1
    for i in range(1, n):
        numList.append(i)
    for x, y in zip(numList, argv):
        print("{}: {}".format(x, y))


if __name__ == "__main__":
    print_args()
