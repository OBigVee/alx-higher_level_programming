#!/usr/bin/python3
"""function finds a peak in a list of unsorted integers."""


from audioop import reverse


def find_peak(list_of_integers):
    """find the peak of a list"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        # sort in descending order
        print(list_of_integers.sort(reverse=True))
        return list_of_integers[0]
