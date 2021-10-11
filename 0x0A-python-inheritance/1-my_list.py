#!/usr/bin/python3
"""defines a class MyList that inherits from list"""


Class MyList(list):
    """ MyList inherit list object"""
    
    def __init__(self,):
        super().__init__()
        
    def print_sorted(self):
        """ sort and print list in ascending order"""
        print(sorted(self))
