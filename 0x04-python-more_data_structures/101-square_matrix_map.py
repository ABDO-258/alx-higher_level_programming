#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda row: list(map(lambda y: y * y, row)), matrix))
