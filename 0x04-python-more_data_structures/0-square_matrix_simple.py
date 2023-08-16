#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i, row in enumerate(matrix):
        new_row = []
        for j, num in enumerate(row):
            new_row.append(num * num)
        new_matrix.append(new_row)
    return new_matrix
