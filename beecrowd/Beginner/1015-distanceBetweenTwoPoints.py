# 1015-distance.py
# Problem: Distance Between Two Points
# Link: https://judge.beecrowd.com/en/problems/view/1015
# Solved on: 2024-08-18

import math

def distance():
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    distanceXY = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    print(f'{distanceXY:.4f}')

distance()