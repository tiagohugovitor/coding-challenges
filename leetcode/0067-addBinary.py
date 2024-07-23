# 0067-addBinary.py
# Problem: Add Binary
# Link: https://leetcode.com/problems/add-binary/description/
# Solved on: 2024-07-21

# Time complexity: O(max(n, m))
# Space complexity: O(max(n, m))
# Description: This function performs binary addition of two binary strings `a` and `b`, returning their sum as a binary string.
# It iterates through both strings from the end, calculating the sum bit by bit while managing carry-over. It handles cases where 
# the strings are of different lengths by continuing the addition for the remaining bits of the longer string. Finally, if there's
# a carry left, it prepends '1' to the result.

def addBinary(a, b):
    sum = ''
    num1 = len(a) - 1
    num2 = len(b) - 1
    carry = 0

    while num1 >= 0 and num2 >= 0:
        bit = int(a[num1]) + int(b[num2]) + carry
        if bit > 1:
            carry = 1
            bit = 1 if bit == 3 else 0
        else:
            carry = 0
        sum = str(bit) + sum
        num1 -= 1
        num2 -= 1

    while num1 >= 0:
        bit = int(a[num1]) + carry
        if bit > 1:
            carry = 1
            bit = 0
        else:
            carry = 0
        sum = str(bit) + sum
        num1 -= 1

    while num2 >= 0:
        bit = int(b[num2]) + carry
        if bit > 1:
            carry = 1
            bit = 0
        else:
            carry = 0
        sum = str(bit) + sum
        num2 -= 1

    if carry == 1:
        sum = '1' + sum
    
    return sum

print(addBinary('1010','1011'))
