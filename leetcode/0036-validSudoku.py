# 0036-validSudoku.py
# Problem: Valid Sudoku
# Link: https://leetcode.com/problems/valid-sudoku/description/
# Solved on: 2024-08-14

# Time complexity: O(1)
# Space complexity: O(1)
# Description: This function checks whether a given 9x9 Sudoku board is valid according to Sudoku rules. It iterates 
# through each row, column, and 3x3 sub-box, using helper functions to ensure there are no duplicate digits (ignoring empty 
# cells). If any row, column, or sub-box contains duplicates, the function returns `False`. Otherwise, it returns `True`, 
# indicating the board is valid. The time complexity is O(1) since the board size is fixed, and the space complexity is also 
# O(1) due to the use of constant-size auxiliary space.

def validSudoku(board):
    def isValidRow(board, row):
        count = [0] * 10
        for i in range(0,9):
            if board[row][i] != '.':
                count[int(board[row][i])] += 1
                if count[int(board[row][i])] > 1:
                    return False
        return True

    def isValidColumn(board, column):
        count = [0] * 10
        for i in range(0,9):
            if board[i][column] != '.':
                count[int(board[i][column])] += 1
                if count[int(board[i][column])] > 1:
                    return False
        return True


    def isValidSubBox(board, subBox):
        count = [0] * 10
        for i in range(0,9):
            if board[(i//3) + (subBox // 3) * 3][(i%3) + (subBox % 3) * 3] != '.':
                count[int(board[(i//3) + (subBox // 3) * 3][(i%3) + (subBox % 3) * 3])] += 1
                if count[int(board[(i//3) + (subBox // 3) * 3][(i%3) + (subBox % 3) * 3])] > 1:
                    return False
        return True

    for i in range(0,9):
        isValid = (isValidRow(board, i) and
            isValidColumn(board, i) and
            isValidSubBox(board, i))
        if not isValid:
            return False
        
    return True

print(validSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))