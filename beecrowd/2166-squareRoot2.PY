# 2166-squareRoot2.py
# Problem: Fast Fibonacci
# Link: https://judge.beecrowd.com/en/problems/view/2166
# Solved on: 2024-08-30

import math

def squareRoot2():
    number = int(input())
    if number == 0:
        solution = 1.0
    else:
        solution = 2
        for _ in range(number - 1):
            solution = 2 +  1/ solution
        solution = 1 + 1/solution
    print(f'{solution:.10f}')
 

squareRoot2()
