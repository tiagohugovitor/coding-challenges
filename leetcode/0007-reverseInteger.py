# 0007-reverseInteger.py
# Problem: Reverse Integer
# Link: https://leetcode.com/problems/reverse-integer/description/
# Solved on: 2024-07-19

# Time complexity: O(log(n))
# Space complexity: O(1)
# Description: This function reverses the digits of a 32-bit signed integer. 
# It first determines the sign of the integer and works with its absolute value.
# It then constructs the reversed number by repeatedly extracting the last digit and appending it to the result.
# The function also handles overflow by returning 0 if the reversed integer exceeds the 32-bit signed integer range.

def reverse(x):
    sign = -1 if x<0 else 1
    x *= sign
    reversed = 0
    while (x > 0):
        reversed *= 10
        reversed += x%10
        x //= 10

    reversed *= sign

    if reversed > 2 ** 31 - 1 or reversed < -2 ** 31:
        return 0

    return reversed

print(reverse(-32))