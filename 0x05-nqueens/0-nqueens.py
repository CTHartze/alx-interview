#!/usr/bin/env python3
"""Solves the N Queens problem"""

import sys


def is_safe(board, row, col, N):
    # Check if no queen threatens the given position
    for i in range(col):
        if board[i][0] == row or \
           board[i][1] == col or \
           abs(board[i][0] - row) == abs(board[i][1] - col):
            return False
    return True

def solve_n_queens_util(board, col, N, solutions):
    # Base case: If all queens are placed
    if col == N:
        solutions.append(board[:])
        return
    
    # Try placing queen in each row of the current column
    for row in range(N):
        if is_safe(board, row, col, N):
            board[col] = (row, col)
            solve_n_queens_util(board, col + 1, N, solutions)
            board[col] = (-1, -1)

def solve_n_queens(N):
    # Initialize the board
    board = [(-1, -1)] * N
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions

def print_solution(solution):
    for i, pos in enumerate(solution):
        if i != 0:
            print(", ", end='')
        print("[{}, {}]".format(pos[1], pos[0]), end='')
    print()

def main():
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for solution in solutions:
        print_solution(solution)

if __name__ == "__main__":
    main()
