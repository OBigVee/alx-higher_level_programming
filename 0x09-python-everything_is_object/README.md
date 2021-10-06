# Python - Everything is object
![image](https://github.com/OBigVee/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/py-tips.jpg)
### Background Context
Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>> 
```
OK. But what about this?

```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 
```
![image](https://github.com/OBigVee/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/tip-py.gif)  

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should read all documentation first (as usual :)), then take the time to think and brainstorm with your peers about what you think and why. Try to do this without coding anything for a few hours.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don’t go this route. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types. The biggest mandatory task is the blog post and it will count for 50% of the total score of the project.

Note that during interviews for Python positions, you will most likely have to answer to these type of questions.

All your answers should be only one line in a file. No space before or after the answer.


## Resources
**Read or watch:**

* [9.10. Objects and values](https://alx-intranet.hbtn.io/rltoken/MrtBogRzYETxnSKG97E7Sg)
* [9.11. Aliasing](https://alx-intranet.hbtn.io/rltoken/Ro-7kVXtmWyAeOXEw7RhSg)
* [Immutable vs mutable types](https://alx-intranet.hbtn.io/rltoken/X1lEmkwQRWI3fP4W7bq_qw)
* [Mutation](https://alx-intranet.hbtn.io/rltoken/HpKOdgDg6GIoBoG0UPOgPA) (Only this chapter)
* [9.12. Cloning lists](https://alx-intranet.hbtn.io/rltoken/HpKOdgDg6GIoBoG0UPOgPA)
* [Python tuples: immutable but potentially changing](https://alx-intranet.hbtn.io/rltoken/NZIom4L-tS0HjpY_uEVr9A)

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/CAr4Pk5CqfDCFIW0cq683Q), without the help of Google:

### General
* Why Python programming is awesome
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions
### Requirements
#### Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using wc
#### `.txt` Answer Files
* Only one line
* No Shebang
* All your files should end with a new line

