# 2968-hourOfRun.py
# Problem: Hour for a Run
# Link: https://judge.beecrowd.com/en/problems/view/2968
# Solved on: 2024-10-16

import math

def hourOfRun():
    laps, signs = map(int, input().split())
    
    totalSigns = laps * signs

    for i in range(1, 10):
        neededSigns = math.ceil(totalSigns * i / 10)
        if i != 9:
            print(f'{neededSigns} ', end='')
        else:
            print(f'{neededSigns}')

hourOfRun()
