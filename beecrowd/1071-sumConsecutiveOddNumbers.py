# 1071-sumConsecutiveOddNumbers.py
# Problem: Six Odd Numbers
# Link: https://judge.beecrowd.com/en/problems/view/1070
# Solved on: 2024-08-19

def sumConsecutiveOddNumbers():
    x = int(input())
    y = int(input())

    if y < x:
        x, y = y, x

    sum = 0

    for i in range(x + 1, y):
        if i % 2 != 0:
            sum += i

    print(f'{sum}')

sumConsecutiveOddNumbers()