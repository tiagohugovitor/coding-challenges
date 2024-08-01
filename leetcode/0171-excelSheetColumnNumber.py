# 0171-excelSheetColumnNumber.py
# Problem: Excel Sheet Column Number
# Link: https://leetcode.com/problems/excel-sheet-column-number/description/
# Solved on: 2024-08-01

# Time complexity: O(n)
# Space complexity: O(1)
# Description: This function converts an Excel column title (e.g., "A", "Z", "AA") to its corresponding column number.
# It iterates through each character of the input string `columnTitle` from right to left, calculates its value 
# by subtracting 64 from its ASCII code, and multiplies it by the appropriate power of 26. The results are then summed 
# to obtain the final column number.

def titleToNumber(columnTitle):
    pow = 1
    columnNumber = 0
    for i in range(len(columnTitle) - 1, -1, -1):
        charValue = (ord(columnTitle[i]) - 64) * pow
        pow *= 26
        columnNumber += charValue

    return columnNumber

print(titleToNumber('AAA'))