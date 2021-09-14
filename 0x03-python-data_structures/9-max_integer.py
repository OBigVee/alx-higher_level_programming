#!/usr/bin/python3
def max_integer(my_list=[]):
    #  function that finds the biggest integer of a list.
    max = 0
    min = 0
    for val in range(len(my_list)):
        if my_list[val] > my_list[val+1]:
          max = my_list[val]
          return max
