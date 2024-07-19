# 0058-lengthOfLastWord.py
# Problem: Length of Last Word
# Link: https://leetcode.com/problems/length-of-last-word/description/
# Solved on: 2024-07-18

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function calculates the length of the last word in a given string.
# It iterates through the string from the end to the beginning, counting the characters of the last word.
# When a non-space character is found, it starts counting until a space is encountered after a word has been found.
# The final size is the length of the last word in the string.

def lengthOfLastWord(s):
    size = 0
    charFound = False
    for char in range(len(s) - 1, -1, -1):
        if s[char] != ' ':
            size += 1
            charFound = True
        else:
            if charFound:
                break                
    return size
    
print(lengthOfLastWord('   fly me   to   the moon  '))