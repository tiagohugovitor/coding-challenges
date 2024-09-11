# 1011-sphere.py
# Problem: Sphere
# Link: https://judge.beecrowd.com/en/problems/view/1011
# Solved on: 2024-08-18

def sphere():
    r = float(input())
    pi = 3.14159
    sphere = (4.0/3) * pi * (r ** 3)
    print(f'VOLUME = {sphere:.3f}')

sphere()