# 1541-buildingHouses.py
# Problem: Building Houses
# Link: https://judge.beecrowd.com/en/problems/view/1541
# Solved on: 2024-08-25

import math

def buildingHouses():
    
    while True:
        case = input().split()
        a = int(case[0])
        if a == 0:
            break
        b = int(case[1])
        c = int(case[2])

        size = (100 * a * b)/ c
        side = int(math.floor(math.sqrt(size)))
        print(side)

buildingHouses()