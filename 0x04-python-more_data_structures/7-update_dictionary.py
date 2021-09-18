#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
#     for keys, values in a_dictionary.items():
      if key in a_dictionary:
          a_dictionary[key] = value
          return a_dictionary
      else:
          a_dictionary[key] = value
          return a_dictionary
        
   
