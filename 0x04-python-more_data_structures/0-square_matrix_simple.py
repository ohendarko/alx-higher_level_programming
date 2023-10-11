#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_mat = []
    for r in matrix:
        sq_r = [x**2 for x in r]
        sq_mat.append(sq_r)
    return sq_mat
