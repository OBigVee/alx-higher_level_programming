#!/usr/bin/python3
""" scripts add all arguments to a list and then save them to a line"""


import json
import sys


if __name__ == "__main__":
    save_to_json = __import__("5-save_to_json_file").save_to_json_file
    load_json file =__import__("6-load_from_json_file.py").laod_from_json_file
    try:
        file = "add_time.json"
        load_json_file(file)
   except:
      file = [] 
   file.extend(sys.argv[1:])
      save_to_json_(file, "add_item.json")
