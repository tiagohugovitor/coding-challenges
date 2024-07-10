# 0009-palindromeNumber.py
# Problem: Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/description/
# Solved on: 2024-07-07

# Time complexity: O(log(n)) base 10.
# Description: This function checks if an integer is a palindrome by reversing its
# digits (extracting digits from the end one by one) and comparing with the original number.


def isPalindrome(x):
    if x < 0:
        return False
    temp = x
    reversed_number = 0
    while temp > 0:
        reversed_number = reversed_number * 10 + temp % 10
        temp //= 10
    return x == reversed_number

print(isPalindrome(121))