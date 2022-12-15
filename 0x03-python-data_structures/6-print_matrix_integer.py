#!/usr/bin/python3
""" function prints a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            print("{:d}".format(i[j]), end=" " * (j < len(i) - 1))
        print()
