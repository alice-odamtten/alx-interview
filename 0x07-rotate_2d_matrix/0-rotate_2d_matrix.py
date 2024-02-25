#!/usr/bin/python3
'''a module to Rotate 2D Matrix'''


def rotate_2d_matrix(matrix):
    '''the function to rotate matrix'''
    matrix[:] = [list(row) for row in zip(*matrix[::-1])]
