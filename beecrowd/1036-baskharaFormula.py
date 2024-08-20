# 1036-baskhara.py
# Problem: Baskhara's Formula
# Link: https://judge.beecrowd.com/en/problems/view/1036
# Solved on: 2024-08-18

import math

def baskhara():

    a, b, c = map(float, input().split())
    delta = b**2 - 4 * a * c
    if delta < 0 or a == 0:
        print('Impossivel calcular')
    else:
        root1 = (- b + math.sqrt(delta))/(2*a)
        root2 = (- b - math.sqrt(delta))/(2*a)

        print(f'R1 = {root1:.5f}')
        print(f'R2 = {root2:.5f}')

baskhara()