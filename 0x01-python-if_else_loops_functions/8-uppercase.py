#!/usr/bin/python3
"""
function prints a string in uppercase followed by a new line
"""
"""
def uppercase(str):
    for i in range(len(str)):
        uni_code = ord(str[i])
        if (uni_code >= 97 and uni_code <= 122):
            uni_code -= 32
        print("{}".format(chr(uni_code)), end="")
    print()
"""
def uppercase(str):
    '''
    Prints a string, converting lowercase characters to uppercase
    Parameters:
    str (str): The string to print
    '''
    txt = ''.join(str) + '\n'
    for i in range(len(txt)):
        c = ord(txt[i])
        is_lower = (c >= ord('a')) and (c <= ord('z'))
        offset = (1 << 5) if is_lower else 0
        print('{:c}'.format(c - offset), end='')
