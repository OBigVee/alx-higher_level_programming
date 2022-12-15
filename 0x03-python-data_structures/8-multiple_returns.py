#!/usr/bin/python3
def multiple_returns(sentence):
    """ function returns a tuple with lenght of a string
    and its first character
    """
    if sentence is None:
        return None
    else:
        t_len = len(sentence)
        char = sentence[0]
        return (t_len, char)
