#!/usr/bin/python3
"""Rotate a 2d Matrix 90 degrees"""


def rotate_2d_matrix(matrix):
    """rotate a 2d matrix"""
    n = len(matrix)
    for i in range(int(n / 2)):  # 0
        y = (n - i - 1)  # 2
        for j in range(i, y):  # 0, 1
            x = (n - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tmp
