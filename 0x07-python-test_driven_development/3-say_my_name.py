#!/usr/bin/python3
""" function prints <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """ function takes two arguments
        Args:
            first_name(str): first name
            last_name(str): last_name
    """
    
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print ("My name is {} {}".format(first_name, last_name))
