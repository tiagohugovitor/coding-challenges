# 1160-populationIncrease.py
# Problem: Population Increase
# Link: https://judge.beecrowd.com/en/problems/view/1160
# Solved on: 2024-08-22

import math

def populationIncrease():
    tests = int(input())
    for _ in range(tests):
        testInput = input().split()
        pA, pB = int(testInput[0]), int(testInput[1])
        gA, gB = float(testInput[2]), float(testInput[3])

        count = 0

        while count < 101 and pA <= pB:
            pA += math.floor(pA * gA /100)
            pB += math.floor(pB * gB /100)
            count += 1

        if count == 101:
            print('Mais de 1 seculo.')
        
        else:
            print(f'{count} anos.')

populationIncrease()