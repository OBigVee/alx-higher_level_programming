#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print("{:d}".format(matrix[row][col]), end='')
            if col != (len(matrix[row]) - 1):
                print(" ", end='')
        print()
