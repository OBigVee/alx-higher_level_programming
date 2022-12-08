#!/usr/bin/python3
"""
function prints the last digit of a number
"""


def print_last_digit(number):
    divisor = 10
    """if(number >=0 and number < 10):
        last_digit = number
    elif(number > 10 and <=99):
        last_digit = number % divisor
    elif(number >= 100):
        last_digit = number % (divisor * divisor)
        """
    print(abs(number) % 10, end="")
    return abs(number) % 10
