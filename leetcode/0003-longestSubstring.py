# 0003-longestSubstring.py
# Problem: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Solved on: 2024-07-21

# Time complexity: O(n)
# Space complexity: O(n)
# Description: This function finds the length of the longest substring in a given string that does not contain repeating characters.
# It uses a sliding window approach with two pointers, left and right, to maintain the current window of unique characters.
# A dictionary is used to store the last seen index of each character. If a character is encountered that is already in the
# current window, the left pointer is moved to the right of the previous occurrence of that character. The function updates
# the maximum size of the substring whenever a longer unique substring is found.

def longestSubstring(string):
    seen = {}
    left = 0
    right = 0
    maxSize = 0
    while right < len(string):
        char = string[right]
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        else:
            maxSize = max(maxSize, right - left + 1)
        seen[char] = right
        right += 1
    
    return maxSize


print(longestSubstring('pwwkew'))