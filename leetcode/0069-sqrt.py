# 0069-sqrt.py
# Problem: Sqrt(x)
# Link: https://leetcode.com/problems/sqrtx/description/
# Solved on: 2024-07-29

# Time complexity: O(log n)
# Description: This function employs a binary search approach to solve the sqrt problem.
# It searches for the root in the range 0 to x//2 + 1, always dividing the search space in half.

def mySqrt(x):
    if x == 0 or x == 1:
        return x
    
    left = 0
    right = x // 2 + 1

    while left <= right:
        mid = (right + left) // 2

        if mid * mid <= x and (mid + 1) * (mid + 1) > x:
            break
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
    
    return mid

print(mySqrt(5))