#!/usr/bin/python3
"""
program that prints all numbers from 0 to 98 in decimal and in hexadecimal
(as in the following example)
You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module
"""
[print("{:d} = {}".format(i, hex(i))) for i in range(99)]
