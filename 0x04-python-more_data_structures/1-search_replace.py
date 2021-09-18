#!/usr/bin/python3
def search_replace(my_list, search, replace):
    _list = []
    for element in my_list:
        if element == search:
            _list.append(replace)
        else :
            _list.append(element)
    return _list 
