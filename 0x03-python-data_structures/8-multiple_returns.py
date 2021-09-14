#!/usr/bin/python3
def multiple_returns(sentence):
    # Write a function that returns a tuple with 
    # the length of a string and its first character.
    if sentence == "":
        return (len(sentence), None)
    else:
        result = len(sentence),sentence[0]
    return result
