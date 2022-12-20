#!/usr/bin/python3
"""function returns a key with the biggest integer value"""


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    big_val = 0
    big_key = ""
    for key, val in a_dictionary.items():
        if val > big_val:
            big_val = val
            big_key = key
    return big_key
