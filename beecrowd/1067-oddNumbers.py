# 1067-oddNumbers.py
# Problem: Odd Numbers
# Link: https://judge.beecrowd.com/en/problems/view/1067
# Solved on: 2024-08-19

def oddNumbers():
    value = int(input())

    for i in range(1, value + 1, 2):
        print(f'{i}')

oddNumbers()