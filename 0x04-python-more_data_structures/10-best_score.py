#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score = float('-inf')
    # or use 0 for score since we know that all values are integers
    best_key = None
    for key, value in a_dictionary.items():
        if value > score:
            score = value
            best_key = key
    return best_key
