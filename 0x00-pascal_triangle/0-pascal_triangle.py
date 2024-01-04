#!/usr/bin/python3

""" Pascal's Triangle """

def pascal_triangle(n):
    """ Returns a list of lists of integers representing the Pascal’s triangle of n 
        If n <= 0, return an empty list
        Args: n (int): number of rows
        Returns: list of lists of integers
    """

    if n <= 0:
        return []
    pasc_tri = []
    for i in range(n):
        row = [1]

        for j in range(1, i):
            row.append(pasc_tri[i - 1][j - 1] + pasc_tri[i - 1][j])
        
        if i > 0:
            row.append(1)
        
        pasc_tri.append(row)

    return pasc_tri