# 0014-longestCommonPrefix.py
# Problem: Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/description/
# Solved on: 2024-07-18

# Time complexity: O(n * m)
# Space complexity: O(1)
# Description: This function finds the longest common prefix string amongst an array of strings.
# It iterates through the characters of the strings, comparing them until a mismatch is found or the end of one of the strings is reached.
# It returns the longest common prefix identified, or an empty string if there is no common prefix.

def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    isEqual = True
    index = -1 
    while isEqual:
        index += 1
        for i in range(0, len(strs) - 1):
            if len(strs[i]) - 1 < index or len(strs[i+1]) -1 < index or strs[i][index] != strs[i+1][index]:
                isEqual = False
                break
    index -= 1
    answer = ''
    while index >= 0:
        answer = strs[0][index] + answer
        index -= 1
    return answer

print(longestCommonPrefix(["flower","flow","flight"]))