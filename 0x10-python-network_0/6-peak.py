#!/usr/bin/python


def find_peak(list_of_integers):
    """function finds the peak value
    of list_of_integer
    """

    peak = None
    n = len(list_of_integers)

    # empty list
    if n == 0:
        return peak

    # check the first element
    if n >= 1 and list_of_integers[0] >= list_of_integers[1]:
        peak = list_of_integers[0]
        return peak

    # check the last element
    if n >= 2 and list_of_integers[n - 1] >= list_of_integers[n - 2]:
        peak = list_of_integers[n - 1]
        return peak

    # iterate through the rest of list_of_integer
    for i in range(1, n - 1):
        if (
            list_of_integers[i] >= list_of_integers[i - 1]
            and list_of_integers[i] >= list_of_integers[i + 1]
        ):
            peak = list_of_integers[i]
            return peak
