#!/usr/bin/python3
"""
program prints ASCII alphabet int lowrcase not followed by a new line
print all the letters execept q and e
You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module
"""
for i in range(26):
    if ord("a") + i != 101 and ord("a") + i != 113:
        print("{:c}".format(ord('a') + i), end="")
    else:
        continue
