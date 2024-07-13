# 0050-pow.py
# Problem: Pow(x, n)
# Link: https://leetcode.com/problems/powx-n/description/
# Solved on: 2024-07-13

# Time complexity: O(n).
# Description: This function implements the power function using brute force.
# It iterates 'n' times and multiplies 'x' by itself in each iteration.

def iterativePow(x,n):
    if n < 0:
        return 1/iterativePow(x,-n)
    total = 1
    for i in range(n):
        total *= x
    return total

# Time complexity: O(log n).
# Description: This function implements the power function using the divide and conquer technique.
# It recursively divides the problem into subproblems of size n/2.

def divideAndConquerPow(x,n):
    if n < 0:
        return 1/divideAndConquerPow(x,-n)
    if n == 0:
        return 1
    if n%2 == 0:
        divided = divideAndConquerPow(x, (n/2))
        return divided * divided
    else:
        divided = divideAndConquerPow(x, ((n-1)/2))
        return divided * x * divided
    
print(divideAndConquerPow(2,-2))