#!/usr/bin/python3
def safe_print_list_intergers(my_list=[], x=0):
    count = 0
    for element in range(0,x):
        try:
            print("{:d}".format(my_list[element]), end="")
            count = 1
        except TypeError:
            break
        except ValueError:
            pass
        except IndexError:
            break
    print()
    return count
