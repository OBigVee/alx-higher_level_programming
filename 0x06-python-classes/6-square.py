#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size
    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            
    @size.setter
    def position(self,value):
        if type(value) != tuple:
            raise TypeError("position must be tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be tuple of 2 positive integers")
        elif type(value[0]) and type(value[1]) != int:
            raise TypeError("position must be tuple of 2 positive integers")
        elif value[0] and value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
            
        

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
        
