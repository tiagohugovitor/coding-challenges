# 2164-fastFibonacci.py
# Problem: Fast Fibonacci
# Link: https://judge.beecrowd.com/en/problems/view/2164
# Solved on: 2024-08-30

import math

def fastFibonacci():
    number = int(input())
    squaredRoot5 = math.sqrt(5)
    fibonacci = (pow((1 + squaredRoot5)/2, number) - (pow((1 - squaredRoot5)/2, number)))/ squaredRoot5

    print(f'{fibonacci:.1f}')

fastFibonacci()
