#!/usr/bin/python3
import sys
argv = sys.argv[1:]
n = len(argv)
numList = []
print("{} arguments:".format(n))

n = len(argv) + 1

for i in range(1, n):
    numList.append(i)

for x, y in zip(numList, argv):
    print("{}: {}".format(x, y))
