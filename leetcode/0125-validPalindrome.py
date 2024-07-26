# 0125-validPalindrome.py
# Problem: Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/description/
# Solved on: 2024-07-25

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function checks if a given string is a palindrome, considering only alphanumeric characters and ignoring case differences.
# It uses two helper functions: isAlphaNumeric to check if a character is alphanumeric, and toLowercase to convert uppercase characters to lowercase.
# The function employs a two-pointer technique to compare characters from the beginning and end of the string, moving towards the center.
# Non-alphanumeric characters are skipped, and comparisons are case-insensitive.

def isPalindrome(str):
    def isAlphaNumeric(char):
        asciiValue = ord(char)
        return ((asciiValue > 47 and asciiValue < 58) or
            (asciiValue > 64 and asciiValue < 91) or 
            (asciiValue > 96 and asciiValue < 123))

    def toLowercase(char):
        asciiValue = ord(char)
        if (asciiValue > 64 and asciiValue < 91):
            return chr(asciiValue + 32)
        return char

    left = 0
    right = len(str) - 1
    while left < right:
        if not isAlphaNumeric(str[left]):
            left += 1
        elif not isAlphaNumeric(str[right]):
            right -= 1
        elif toLowercase(str[right]) == toLowercase(str[left]):
            right -= 1
            left += 1
        else:
            return False
    return True

print(isPalindrome('A man, a plan, a canal: Panama'))