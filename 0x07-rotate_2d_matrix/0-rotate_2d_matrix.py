#!/usr/bin/python3
"""
Module: rotate_2d_matrix
"""

from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.
    """
    # Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
