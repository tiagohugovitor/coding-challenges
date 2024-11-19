# 1221-fastPrimeNumber.py
# Problem: Fast Prime Number
# Link: https://judge.beecrowd.com/en/problems/view/1221
# Solved on: 2024-11-18

import sys
import math

def fastPrimeNumber():
    input_data = sys.stdin.read().splitlines()
    i = 1


    for _ in range(int(input_data[0])):
        number = int(input_data[i])
        i += 1
        if number == 1 or number == 2:
            print('Prime')
            continue
        breakpoint = int(math.sqrt(number)) + 1
        isPrime = True
        for j in range(2, breakpoint):
            if number % j == 0:
                isPrime = False
                break

        if isPrime:
            print('Prime')
        else:
            print('Not Prime')
        
fastPrimeNumber()
