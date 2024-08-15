# 0441-arrangeCoins.py
# Problem: Arranging Coins
# Link: https://leetcode.com/problems/arranging-coins/description/
# Solved on: 2024-08-15

# Time complexity: O(log n)
# Space complexity: O(log n)
# Description: This recursive function determines the number of complete rows of coins that can be arranged with `n` coins, 
# where each row contains one more coin than the previous row. The inner function `arrangeCoins` recursively subtracts 
# the number of coins used for each row (`line`) from the total `coins` and increments the row number until the remaining 
# coins are insufficient for the next row.

def arrangeCoinsRecursive(n):
    def arrangeCoins(coins, line):
        if line > coins:
            return line - 1
        return arrangeCoins(coins - line, line + 1)
    
    return arrangeCoins(n, 1)

# Time complexity: O(sqrt n)
# Space complexity: O(1)
# Description: This iterative function calculates the number of complete rows that can be formed with `n` coins, where each 
# row requires an incrementally increasing number of coins. It iteratively adds rows and subtracts the number of coins 
# required for each row from `n` until `n` is less than the next row's required coins. This approach efficiently handles 
# the problem with linear time complexity relative to the number of rows and constant space complexity.

def arrangeCoinsIterative(n):
    line = 0

    while line < n:
        line += 1
        n -= line
    
    return line

# Time complexity: O(1)
# Space complexity: O(1)
# Description: This function calculates the maximum number of complete rows that can be formed with `n` coins using the 
# arithmetic progression sum formula. It computes the number of rows by solving the quadratic equation derived from the 
# sum formula for the first `k` positive integers.

import math

def arrangeCoinsMath(n):
    k = (-1 + math.sqrt(1 + 8 * n)) / 2
    return int(k)

print(arrangeCoinsIterative(5))