#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number[-1] > 5:
    print("the last digit of {:d} is {:d} and is greater than 5".format(number,number[-1]))
elif number[-1] < 6:
    print("the last digit of {:d} is {:d} and is less than 6 and not 0".format(number,number[-1]))
else:
    print("the last digit of {:d} is {:d} and is 0 ".format(number, number[-1]))
