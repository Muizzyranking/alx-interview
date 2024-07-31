#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for n in range(n):
        row = []
        for y in range(n+1):
            if y == 0 or y == n:
                row.append(1)
            else:
                row.append(triangle[n-1][y-1] + triangle[n-1][y])

        triangle.append(row)

    return triangle
