#!/bin/bash/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    for i in range(0, 2):
        if len(tuple_a) < i+1:
            tuple_a += (0,)
        if len(tuple_b) < i+1:
            tuple_b += (0,)
        res.append(tuple_a[i] + tuple_b[i])
    return tuple(res)
