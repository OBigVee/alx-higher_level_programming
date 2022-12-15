#!/usr/bin/python3
""" function returns a tuple with lenght of a string
and its first character"""


def multiple_returns(sentence):
    if sentence is None:
        return None
    else:
        t_len = len(sentence)
        char = sentence[0]
        return (t_len, char)
