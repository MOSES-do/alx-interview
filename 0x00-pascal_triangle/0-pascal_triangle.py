#!/usr/bin/python3
"""
returns a list of lists of integers of Pascal’s
triangle n
"""


def pascal_triangle(n):
    """representing the Pascal’s"""

    last = 1
    if n <= 0:
        return []

    tr = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(tr[i-1][j - 1] + tr[i-1][j])
        row.append(last)
        tr.append(row)
    return tr
