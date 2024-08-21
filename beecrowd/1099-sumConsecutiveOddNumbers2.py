# 1099-sumConsecutiveOddNumbers.js
# Problem: Sum of Consecutive Odd Numbers II
# Link: https://judge.beecrowd.com/en/problems/view/1099
# Solved on: 2024-08-20

def sumConsecutiveOddNumbers():
    n = int(input())
    for _ in range(0, n):
        x, y = map(int, input().split())
        sum = 0
        if x > y:
            x, y = y, x
        for i in range(x + 1, y):
            if i % 2 != 0:
                sum += i
        print(f'{sum}')

sumConsecutiveOddNumbers()
