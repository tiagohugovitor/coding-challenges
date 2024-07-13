# 0070-climbingStairs.py
# Problem: Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/description/
# Solved on: 2024-07-12

# Time complexity: O(n)
# Space complexity: O(n)
# Description: This function uses dynamic programming to calculate the number of distinct ways
# to climb a staircase with 'n' steps, storing results in an array.

def climbingStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    amountOfWays = [0] * (n + 1)
    amountOfWays[1] = 1
    amountOfWays[2] = 2

    for i in range(3, n + 1):
        amountOfWays[i] = amountOfWays[i - 1] + amountOfWays[i - 2]
    
    return amountOfWays[n]

print(climbingStairs(2))