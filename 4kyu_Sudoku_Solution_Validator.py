# ------------------------------------------------------
# Sudoku Background
# Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, 
# so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
# (More info at: http://en.wikipedia.org/wiki/Sudoku)
#
# Sudoku Solution Validator
# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, 
# and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, 
# which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.
#
# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
# ------------------------------------------------------

import numpy as np

def check(arr, diag):
    for line in arr:
        if sum(line) != 45 or len(set(diag)) != 3:
            return False
    return True

def valid_solution(board):
    board_diag = np.diag(board)[:3]
    rotated_board = np.rot90(board)
    rotated_diag = np.diag(rotated_board)[:3]
    return check(board, board_diag) and check(rotated_board, rotated_diag)


if __name__ == '__main__':
    print(valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                          [2, 3, 4, 5, 6, 7, 8, 9, 1],
                          [3, 4, 5, 6, 7, 8, 9, 1, 2],
                          [4, 5, 6, 7, 8, 9, 1, 2, 3],
                          [5, 6, 7, 8, 9, 1, 2, 3, 4],
                          [6, 7, 8, 9, 1, 2, 3, 4, 5],
                          [7, 8, 9, 1, 2, 3, 4, 5, 6],
                          [8, 9, 1, 2, 3, 4, 5, 6, 7],
                          [9, 1, 2, 3, 4, 5, 6, 7, 8]])) # False
    
    print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                          [6, 7, 2, 1, 9, 5, 3, 4, 8],
                          [1, 9, 8, 3, 4, 2, 5, 6, 7],
                          [8, 5, 9, 7, 6, 1, 4, 2, 3],
                          [4, 2, 6, 8, 5, 3, 7, 9, 1],
                          [7, 1, 3, 9, 2, 4, 8, 5, 6],
                          [9, 6, 1, 5, 3, 7, 2, 8, 4],
                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
                          [3, 4, 5, 2, 8, 6, 1, 7, 9]])) # True