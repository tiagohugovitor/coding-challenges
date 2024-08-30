# 2152-approximatePrimeNumber.py
# Problem: Approximate NUmber of Primes
# Link: https://judge.beecrowd.com/en/problems/view/2159
# Solved on: 2024-08-29

import math 

def approximatePrimeNumber():
    number = int(input())
    minimum = number / math.log(number)
    maximum = minimum * 1.25506

    print(f'{minimum:.1f} {maximum:.1f}')
approximatePrimeNumber()
