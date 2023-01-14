#!/usr/bin/python3
"""A Class MyList that inherits from list"""


class MyList(list):
    """MyList class inherits from the list class"""

    def print_sorted(self):
        """method prints the list in ascending"""
        print(sorted(self))
