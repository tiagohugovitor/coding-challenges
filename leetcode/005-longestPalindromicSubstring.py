# 005-longestPalindromicSubstring.py
# Problem: Longest Palindromic Substring
# Link: https://leetcode.com/problems/longest-palindromic-substring/description/
# Solved on: 2024-07-07

# Time complexity: O(n²)
# Description: This function expands around each character and pair of characters to find all possible palindromes.
# The longest palindrome found during these expansions is returned.

def longestPalindrome(s):
    def expandAroundCenter(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    for i in range(len(s)):
        # Odd length palindromes
        palindrome1 = expandAroundCenter(s, i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        
        # Even length palindromes
        palindrome2 = expandAroundCenter(s, i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2
    
    return longest   
