# 0190-reverseBits.py
# Problem: Reverse Bits
# Link: https://leetcode.com/problems/reverse-bits/description/
# Solved on: 2024-08-01

# Time complexity: O(1)
# Space complexity: O(1)
# Description: This function reverses the bits of a given 32-bit unsigned integer n.
# It first converts the integer to its binary representation, stores it in an array of size 32,
# then constructs the reversed binary number by iterating through the array from the end to the
# beginning and calculating the new integer value.

def reverseBits(n):
    binary = [0] * 32
    index = 0
    while n > 0:
        bit = n % 2
        binary[index] = bit
        index += 1
        n //= 2
    result = 0
    pow = 1
    for i in range(len(binary) - 1, -1, -1):
        value = pow * binary[i]
        pow *= 2
        result += value
    
    return result


print(reverseBits(4294967293))