# 0202-happyNumber.py
# Problem: Happy Number
# Link: https://leetcode.com/problems/happy-number/description/
# Solved on: 2024-08-14

# Time complexity: O(log n)
# Space complexity: O(log n)
# Description: This function determines if a number `n` is a "happy number." A happy number is one that eventually reaches 
# 1 when replaced by the sum of the squares of its digits. The function uses a loop to repeatedly calculate this sum, 
# tracking previously visited sums to detect cycles. If the sequence reaches 1, the function returns `True`; if it 
# enters a cycle, it returns `False`. The time and space complexity are O(log n), as the number of digits and sum 
# calculations depend on the logarithm of `n`.

def happyNumber(n):
    visited = [n]
    while n != 1:
        total = 0
        for char in str(n):
            square = int(char) * int(char)
            total += square
        n = total
        if n in visited:
            return False
        visited.append(n)
    return True

print(happyNumber(3))