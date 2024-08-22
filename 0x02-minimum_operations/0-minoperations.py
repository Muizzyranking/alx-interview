#!/usr/bin/python3
"""
This module provides a function to calculate the
minimum number of operations needed to achieve exactly
`n` 'H' characters in a text file using only "Copy All"
and "Paste" operations.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed
    to result in exactly n 'H' characters in the file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations needed.
        Returns 0 if `n` is impossible to achieve.
    """

    if n <= 1:
        return 0

    # Initialize the number of operations to 0
    operations = 0
    # Initialize the divisor to start checking from 2
    divisor = 2

    # Loop until we reduce n to 1
    while n > 1:
        # While n is divisible by the current divisor
        while n % divisor == 0:
            # Perform the operations: (divisor times Paste, and 1 Copy)
            operations += divisor
            # Reduce n by the divisor
            n //= divisor
        # Move to the next divisor
        divisor += 1

    return operations
