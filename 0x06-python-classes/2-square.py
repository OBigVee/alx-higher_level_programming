#!/usr/bin/python3
""" Define a square class """


class Square:
"""Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        return self.size = size

    @property
    def size(self):
        """ size sett """
        return self.__size

    @size.setter
    def size(self, size):
        """ set size"""
        if type(size) != int:
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
