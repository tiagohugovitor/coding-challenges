# 0008-stringToInteger.py
# Problem: String to Integer (atoi)
# Link: https://leetcode.com/problems/string-to-integer-atoi/description/
# Solved on: 2024-07-19

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function converts a string to a 32-bit signed integer, implementing a simplified version of the `atoi` function.
# It processes the string character by character, handling optional leading spaces and an optional sign (+ or -). It then converts
# consecutive digit characters into an integer value. The function handles overflow by clamping the result within the 32-bit signed
# integer range, returning the appropriate boundaries if exceeded.

def myAtoi(s):
    number = 0
    reading = False
    sign = 1
    for char in s:
        if char == ' ':
            if reading:
                break
            continue
        elif char in ('-', '+'):
            if reading:
                break
            else:
                sign = -1 if char == '-' else 1
                reading = True
        elif char >= '0' and char <= '9':
            reading = True
            number *= 10
            number += int(char)
        else:
            break
    
    number *= sign

    if number < - 2 ** 31:
        return - 2 ** 31
    if number > 2 ** 31 - 1:
        return 2 ** 31 - 1
    return number 

print(myAtoi('   +0 123'))