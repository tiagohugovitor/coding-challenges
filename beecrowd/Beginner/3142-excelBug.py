# 3142-excelBug.py
# Problem: Excel Bug
# Link: https://judge.beecrowd.com/en/problems/view/3142
# Solved on: 2024-10-30

import sys

def excelBug():
    for column in sys.stdin:
        column = column.strip()
        if len(column) > 3:
            print('Essa coluna nao existe Tobias!')
            continue

        columnNumber = 0
        for char in column:
            columnNumber = columnNumber * 26 + (ord(char) - ord('A') + 1)

        if columnNumber > 16384:
            print('Essa coluna nao existe Tobias!')
        else:
            print(columnNumber)

excelBug()
