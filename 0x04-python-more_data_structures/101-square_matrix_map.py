#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda row: list(map(lambda y: y * y, row)), matrix))
    return new_matrix
