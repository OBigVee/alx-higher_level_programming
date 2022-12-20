#!/usr/bin/python3
"""function returns a key with the biggest integer value"""


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.keys()) == 0:
        return None
    big_key, big_val = "", 0
    for key, val in a_dictionary.items():
        if val > big_val:
            big_val, big_key = val, key
    return big_key
