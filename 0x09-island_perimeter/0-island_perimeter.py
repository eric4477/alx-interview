#!/usr/bin/python3
"""Defines island perimeter finding function."""

def island_perimeter(grid):
    """
    Return the perimeter of an island.
    The grid represents water by 0 and land by 1.

    Args:
        grid (list): A list of list of integers representing an island.

    Returns:
        int: The perimeter of the island defined in grid.
    """
    perimeter = 0
    height = len(grid)
    width = len(grid[0])

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
