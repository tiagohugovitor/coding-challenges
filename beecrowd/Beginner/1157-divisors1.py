# 1157-divisors1.py
# Problem: Divisors 1
# Link: https://judge.beecrowd.com/en/problems/view/1157
# Solved on: 2024-08-22

def divisors1():
    n = int(input())
    for i in range(1, n+1):
        if n % i == 0:
            print(f'{i}')

divisors1()