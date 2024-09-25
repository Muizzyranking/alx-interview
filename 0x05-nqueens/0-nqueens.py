#!/usr/bin/python3
"""
Module to solve the N-Queens problem
"""
import sys


def is_safe(board, row, col):
    """
    checks if a queen can be placed on board[row][col]

    Args:
        board: list of integers
        row: integer
        col: integer

    Returns:
        True if the queen can be placed, False otherwise
    """
    # Check if a queen can be placed on board[row][col]

    # Check the column for any queens
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """
    Solve the N-Queens problem and append the solution to solutions

    Args:
        N: integer
        row: integer
        board: list of integers
        solutions: list of list of integers
    """
    # Recursive function to solve the problem using backtracking
    if row == N:
        # If all queens are placed successfully, add the solution
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            # Backtrack, the board[row] will be reassigned


def nqueens(N):
    """
    Solve the N-Queens problem

    Args:
        N: integer

    Returns:
        solutions: list of list of integers
    """
    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = nqueens(N)
    for solution in solutions:
        print(solution)
