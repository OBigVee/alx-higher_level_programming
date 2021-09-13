!#/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reverse_list = my_list.reverse()
    for val in reverse_list:
        print("{:d}".format(val))  
