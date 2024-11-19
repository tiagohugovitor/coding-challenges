# 1161-factorialSum.py
# Problem: Factorial Sum
# Link: https://judge.beecrowd.com/en/problems/view/1161
# Solved on: 2024-11-18

import sys

def factorialSum():
    input_data = sys.stdin.read().splitlines()
    i = 0


    factorial = [1, 1]
    while i < len(input_data):
        first, second = map(int, input_data[i].split())
        i += 1
        
        while first >= len(factorial) or second >= len(factorial):
            nextFactorial = factorial[len(factorial) - 1] * len(factorial)
            factorial.append(nextFactorial)

        print(factorial[first] + factorial[second])

factorialSum()
