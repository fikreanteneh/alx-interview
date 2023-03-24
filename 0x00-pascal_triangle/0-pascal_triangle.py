#!/usr/bin/python3
"""
contains the Pascal's Triangle function
"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing
        the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    rows = [[1]]
    for i in range(2,n+ 1):     
        upperRow = rows[-1]
        answer = [0] * ( i )
        answer[0], answer[-1] = 1, 1
        for j in range(1, i-1):
            answer[j] += (upperRow[j-1] + upperRow[j])
        rows.append(answer)
    
    return rows
