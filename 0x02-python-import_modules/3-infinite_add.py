#!/usr/bin/python3
import sys
a = sys.argv[1:]
total = 0

for i in range(len(a)):
    total = total + int(a[i])
print(total)
