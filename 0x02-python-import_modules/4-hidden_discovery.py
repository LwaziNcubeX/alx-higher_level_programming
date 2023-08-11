#!/usr/bin/python3
import hidden_4
import sys

if __name__ == "__main__":
    name = dir(hidden_4)
    check = "_"

    for name in name:
        if name.startswith(check):
            continue
        else:
            print(name)
