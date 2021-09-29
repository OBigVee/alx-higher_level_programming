#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        return self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self,size):
        if type(size) != int:
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
