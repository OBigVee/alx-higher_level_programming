# Resources
#### **Read or watch:**

* [Object Oriented Programming](https://alx-intranet.hbtn.io/rltoken/M-MFweENpRdEfRto_Gzlvg) (Read everything until the paragraph “Inheritance” (excluded))
* [Object-Oriented Programming](https://alx-intranet.hbtn.io/rltoken/u1xlAhNfvrGGIAOf3RuDWw) (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The `__init__` Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “`__str__`- and `__repr__`-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
* [Class and Instance Attributes](https://alx-intranet.hbtn.io/rltoken/aciW9EYvx0WuJ7Ln6rg23A)
* [classmethods and staticmethods](https://alx-intranet.hbtn.io/rltoken/Ij1EnTg02gtIknOkNv4xGA)
* [Properties vs. Getters and Setters](https://alx-intranet.hbtn.io/rltoken/sK_OM5kGeifREANha4dFgQ) (Mainly the last part “Public instead of Private Attributes”)
* [str vs repr](https://alx-intranet.hbtn.io/rltoken/HsiKqylUwlcyIvoFCtlHtg)


Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* Why Python programming is awesome
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method
* What is the special `__init__` method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* What are the special `__str__` and `__repr__` methods and how to use them
* What is the difference between `__str__` and `__repr__`
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain `__dict__` of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the getattr function

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using `wc`

#### **N queens** __________________________________________________________________________________________________________________________________________________________
  
  ![image](https://github.com/OBigVee/alx-higher_level_programming/blob/main/0x08-python-more_classes/Judit-photo1_602x433.jpg)  
  Chess grandmaster [Judit Polgár](https://alx-intranet.hbtn.io/rltoken/bsRwbt64OvYjWaClriv0jg), the strongest female chess player of all time


The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

* Usage: `nqueens N`  
    * If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
* where N must be an integer greater or equal to 4
   * If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
  * If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
* The program should print every possible solution to the problem
  * One solution per line
  * Format: see example
  * You don’t have to print the solutions in a specific order
* You are only allowed to import the sys module


Read: [Queen](https://alx-intranet.hbtn.io/rltoken/dAQmi8RxMnLH-iHBzkz-lw), [Backtracking](https://alx-intranet.hbtn.io/rltoken/TGXZXdY2Awg8m4mSjlrjjA)

```
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4  
[[0, 1], [1, 3], [2, 0], [3, 2]]    
[[0, 2], [1, 0], [2, 3], [3, 1]] 
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6  
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]  
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]  
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]  
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]  
julien@ubuntu:~/0x08. N Queens$
```
