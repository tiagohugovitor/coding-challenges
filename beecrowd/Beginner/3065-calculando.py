# 3065-calculando.py
# Problem: Calculando
# Link: https://judge.beecrowd.com/en/problems/view/3065
# Solved on: 2024-10-23

import re

def calculando():
    tests = 0
    while True:
        tests += 1
        operatorsAmount = int(input())
        if operatorsAmount == 0:
            break
        
        expression = input()
        numbers = re.split(r'[+-]', expression)
        numbers = list(map(int, numbers))
        total = numbers[0]
        index = 1
        for char in expression:
            if char == '+':
                total += numbers[index]
                index += 1
            if char == '-':
                total -= numbers[index]
                index += 1

        print(f'Teste {tests}')
        print(total)
        print()

calculando()
