# 0006-zigzagConversion.py
# Problem: Zigzag Conversion
# Link: https://leetcode.com/problems/zigzag-conversion/description/
# Solved on: 2024-07-19

# Time complexity: O(n)
# Space complexity: O(n)
# Description: This function converts a given string into a zigzag pattern on a given number of rows.
# The characters are arranged in a zigzag pattern and then read line by line. The function processes
# the string by iterating over it in steps of the zigzag cycle length for the first and last lines,
# and alternates between downward and upward movement for the middle lines to collect characters in
# the zigzag pattern.

def convert(s, numRows):
    if numRows == 1:
        return s
    firstAndLastLines = (numRows - 2) * 2 + 2
    zigzag = ''
    for i in range(0, len(s), firstAndLastLines):
        zigzag = zigzag + s[i]

    for i in range(1, numRows - 1):
        down = True
        j = i
        while j < len(s):
            zigzag = zigzag + s[j]
            down = not down
            if down:
                j += (i - 1) * 2 + 2
            else:
                j += ((numRows - 2) - i) * 2 + 2

    for i in range(numRows - 1, len(s), firstAndLastLines):
        zigzag = zigzag + s[i]
    
    return zigzag

print(convert('PAYPALISHIRING', 4))