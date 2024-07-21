# 0028-indexOfFirstOccurrence.py
# Problem: Find the Index of the First Occurrence in a String
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# Solved on: 2024-07-21

# Time complexity: O(n * m)
# Space complexity: O(1)
# Description: This function finds the first occurrence of the substring `needle` in the string `haystack`. It iterates 
# through `haystack` and checks if the substring starting at each position matches `needle`. If a match is found, it 
# returns the index of the first character of `needle` in `haystack`. If no match is found, it returns -1.

def strStr(haystack, needle):
    foundIndex = -1
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            isSubstring = True
            q = 1
            while isSubstring and q < len(needle):
                if q+i >= len(haystack) or haystack[q+i] != needle[q]:
                    isSubstring = False
                q += 1
            if isSubstring:
                foundIndex = i
                break

    return foundIndex

print(strStr('aaa', 'aaaa'))