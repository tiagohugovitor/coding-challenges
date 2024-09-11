# 1159-sumOfConsecutiveEvenNumbers.py
# Problem: Sum of Consecutive Even Numbers
# Link: https://judge.beecrowd.com/en/problems/view/1159
# Solved on: 2024-08-22

def sumOfConsecutiveEvenNumbers():
    x = int(input())
    while x != 0:
        x = x if x % 2 == 0 else x + 1
        sum = (x * 5) + 20
        print(f'{sum}')
        x = int(input())

sumOfConsecutiveEvenNumbers()