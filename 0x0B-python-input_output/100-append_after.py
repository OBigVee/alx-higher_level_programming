#!usr/bin/python3
""" Search and update"""


def append_after(filename="", search_string="", new_string=""):
    content = []
    with open(filename, "r", encoding="utf-8") as fileobject:
        content = fileobject.readlines()
        idx = 0
        # print(content)
        while idx < len(content):
            if search_string in content[idx]:
                # print(content[idx])
                content[idx:idx + 1] = [content[idx], new_string]
                # print(content)
                idx += 1
            idx += 1
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(content)