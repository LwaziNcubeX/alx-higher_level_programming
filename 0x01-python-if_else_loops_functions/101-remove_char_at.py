#!/usr/bin/python3
def remove_char_at(str, n):
    if n < abs(len(str)):
        return str[:n] + str[n+1:]
    elif n == -n:
        return str
    else:
        return str
