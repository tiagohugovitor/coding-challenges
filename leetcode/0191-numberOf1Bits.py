# 0191-numberOf1Bits.py
# Problem: Number of 1 Bits
# Link: https://leetcode.com/problems/number-of-1-bits/description/
# Solved on: 2024-08-01

# Time complexity: O(log n)
# Space complexity: O(1)
# Description: This function calculates the number of '1' bits (Hamming weight) in the binary
# representation of a given integer n. It iterates through each bit of the number, incrementing
# a counter if the bit is '1', and then shifts the number to the right by dividing by 2 until n
# becomes zero.

def hammingWeight(n):
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n = n // 2

    return count

print(hammingWeight(11))