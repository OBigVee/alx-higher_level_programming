#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            row = self.__size
            col = self.__size

            for i in range(row):
                for j in range(col):
                    print("#", end="")
                print("")
        
