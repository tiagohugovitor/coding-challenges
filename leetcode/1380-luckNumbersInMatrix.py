# 1380-luckNumbersInMatrix.py
# Problem: Lucky Numbers in a Matrix
# Link: https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
# Solved on: 2024-07-19

# Time complexity: O(n * m)
# Space complexity: O(n + m)
# Description: This function finds all lucky numbers in a matrix. A lucky number is defined as the
# minimum element in its row and the maximum in its column. The code iterates through the matrix to
# find the minimum number in each row and the maximum number in each column. Then, it checks if the
# indices of the minimum numbers match the indices of the maximum numbers. The matches are returned
# as lucky numbers.

def luckyNumbers(matrix):
    lines = len(matrix)
    columns = len(matrix[0])
    minimum = [0] * lines
    maximum = [0] * columns
    lucky = []
    for i in range(lines):
        for j in range(columns):
            if matrix[i][j] < matrix[i][minimum[i]]:
                minimum[i] = j
            if matrix[i][j] > matrix[maximum[j]][j]:
                maximum[j] = i

    for i in range(len(minimum)):
        if maximum[minimum[i]] == i:
            lucky.append(matrix[i][minimum[i]])

    return lucky

print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))