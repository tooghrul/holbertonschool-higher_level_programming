#!/usr/bin/python3
"""Pascal triangle"""

def pascal_triangle(n):
    """It is a pascal trianle function"""
    if n <= 0:
        return []

    if n == 1:
        return [1]

    pascal = [[1], [1,1]]
    prev_pascal = pascal[1]
    for step in range(3,n+1):
        base = [0 if i != 0 and i != step - 1 else 1 for i in range(step)]
        for i in range(1, step-1):
            base[i] = prev_pascal[i] + prev_pascal[i-1]
        pascal.append(base)
        prev_pascal = base
    return pascal
