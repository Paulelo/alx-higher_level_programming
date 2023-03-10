#!/usr/bin/python3
import sys


def solve_n_queens(n):
    board = [[None for i in range(n)] for j in range(n)]
    result = []
    solve_n_queens_helper(board, 0, result)
    return result


def solve_n_queens_helper(board, col, result):
    if col == len(board):
        # Found a valid solution, add it to result
        queens = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] is not None:
                    queens.append([i, j])
        result.append(queens)
        return

    for row in range(len(board)):
        if is_valid(board, row, col):
            # Place a queen on this row and recurse to the next column
            board[row][col] = True
            solve_n_queens_helper(board, col+1, result)
            board[row][col] = None


def is_valid(board, row, col):
    # Check if it is safe to place a queen at (row, col)
    n = len(board)
    # Check row
    for i in range(col):
        if board[row][i]:
            return False
    # Check diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row+1, n, 1), range(col-1, -1, -1)):
        if board[i][j]:
            return False
    return True


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)
else:
    try:
        int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)
else:
    resu = solve_n_queens(int(sys.argv[1]))
    for solution in resu:
        print(solution)
