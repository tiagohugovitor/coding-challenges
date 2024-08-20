# 1070-sixOddNumbers.py
# Problem: Six Odd Numbers
# Link: https://judge.beecrowd.com/en/problems/view/1070
# Solved on: 2024-08-19

def sixOddNumbers():
    value = int(input())
    value = value + 1 if value % 2 == 0 else value
    for _ in range(0,6):
        print(f'{value}')
        value += 2

sixOddNumbers()