#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""

def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the Pascal triangle"""
    if n <= 0:
        return []

    triangle = [0] * n  # Initialize list for storing rows

    for i in range(n):
        # Define a row and fill first and last idx with 1
        new_row = [0] * (i + 1)
        new_row[0] = 1
        new_row[-1] = 1  # Last element is always 1

        # Calculate the middle elements
        for j in range(1, i):
            new_row[j] = triangle[i - 1][j] + triangle[i - 1][j - 1]

        # Add the new row to the triangle
        triangle[i] = new_row

    return triangle

