# 1093-vampires.py
# Problem: Vampires
# Link: https://judge.beecrowd.com/en/problems/view/1093
# Solved on: 2024-11-19

import math

def vampires():
    while True:
        life1, life2, at, damage = map(int, input().split())
        
        if life1 == 0 and life2 == 0 and at == 0 and damage == 0:
            break
        
        winsNeeded =  math.ceil(life2 / damage)
        probability =  pow(at / 6, winsNeeded) * 100
        
        print(f'{probability:.1f}')

vampires()
