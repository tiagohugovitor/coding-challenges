# 2203-crowstorm.py
# Problem: Crowstorm
# Link: https://judge.beecrowd.com/en/problems/view/2203
# Solved on: 2024-09-02

import math

def crowstorm():
    while True:
        try:
            xf, yf, x1, y1, v1, r1, r2 = map(int, input().split())
            distance = math.sqrt(pow(abs(x1-xf), 2) + pow(abs(y1-yf), 2)) + v1 * 1.5
            if distance > r1 + r2:
                print('N')
            else:
                print('Y')
        except EOFError:
            break

crowstorm()
