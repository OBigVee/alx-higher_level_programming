#!/usr/bin/python3
"""
function prints a string in uppercase followed by a new line
"""
def uppercase(str):
    for i in range(len(str)):
        uni_code = ord(str[i])
        if (uni_code >= 97 and uni_code <= 122):
            uni_code -= 32
        print("{}".format(chr(uni_code)), end="")
    print()
