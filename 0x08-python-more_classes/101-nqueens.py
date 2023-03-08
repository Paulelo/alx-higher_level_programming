#!/usr/bin/python3

def solve_n_queens(n):
    #board = [['.' for i in range(n)] for j in range(n)]
    board = [[list() for i in range(n)] for j in range(n)]
    result = []
    solve_n_queens_helper(board, 0, result)
    print(board)
    print(result)
    return result

def solve_n_queens_helper(board, col, result):
    if col == len(board):
        # Found a valid solution, add it to result
        #result.append([''.join(row) for row in board])
        #result.append(board)
        return

    for row in range(len(board)):
        if is_valid(board, row, col):
            # Place a queen on this row and recurse to the next column
            board[row][0] = row
            board[row][1] = col
            solve_n_queens_helper(board, col+1, result)
            
def is_valid(board, row, col):
    # Check if it is safe to place a queen at (row, col)
    n = len(board)
    # Check row
    for i in range(col):
        if board[row][0] == row and board[row][1] == col:
            return False
    # Check diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == row and board[i][j+1] == col:
            return False
    for i,j in zip(range(row+1, n, 1), range(col-1, -1, -1)):
        if board[i][j] == row and board[i][j+1] == col:
            return False
    return True

resu = solve_n_queens(4)
for solution in resu:
    print(solution)
