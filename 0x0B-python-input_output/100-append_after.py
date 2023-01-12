#!/usr/bin/python3
"""100-append_after.py"""


def append_after(filename="", search_string="", new_string=""):
    """
    append_after: function inserts a line of text to a file,
        after each line containing a specific string
    Args:
        filename(str): name of the file to process
        search_string(str): string to search for with text file file
                            'filname'
        new_string(str): string to insert

        Returns:
            a modified text file with the inserted new_string
    """
    data = []

    with open(filename, mode="r", encoding="utf-8") as file_obj:
        data = file_obj.readlines()
        idx = 0
        while idx < len(data):
            if search_string in data[idx]:
                data[idx:idx + 1] = [data[idx], new_string]
                idx += 1
            idx += 1

    with open(filename, mode="w", encoding="utf-8") as file_obj:
        file_obj.writelines(data)
