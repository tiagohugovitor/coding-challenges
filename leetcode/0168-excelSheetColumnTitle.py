# 0168-excelSheetColumnTitle.py
# Problem: Excel Sheet Column Title
# Link: https://leetcode.com/problems/excel-sheet-column-title/description/
# Solved on: 2024-07-31

# Time complexity: O(log n)
# Space complexity: O(log n)
# Description: This function converts a given column number (as used in Excel) into its corresponding column title.
# It repeatedly computes the character for the current position by using modulo and integer division operations.
# The ASCII value for 'A' is 65, and the characters are computed accordingly and appended to the title string in reverse order.

def convertToTitle(columnNumber):
    title = ''

    while columnNumber > 0:
        charValue = ((columnNumber - 1) % 26) + 65
        char = chr(charValue)
        title = char + title
        columnNumber = ((columnNumber - 1) // 26)

    return title

print(convertToTitle(703))